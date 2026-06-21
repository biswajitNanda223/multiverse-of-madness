import pytest

from .models import Split, SplitType
from .service import SplitwiseService


@pytest.fixture
def splitwise_setup() -> SplitwiseService:
    service = SplitwiseService()
    # Create users
    service.add_user("u1", "Alice", "alice@example.com")
    service.add_user("u2", "Bob", "bob@example.com")
    service.add_user("u3", "Charlie", "charlie@example.com")

    # Create group
    service.create_group("g1", "Trip 2026")
    service.add_user_to_group("g1", "u1")
    service.add_user_to_group("g1", "u2")
    service.add_user_to_group("g1", "u3")

    return service


def test_equal_split(splitwise_setup: SplitwiseService) -> None:
    service = splitwise_setup

    splits = [Split(user_id="u1"), Split(user_id="u2"), Split(user_id="u3")]

    expense = service.add_expense(
        group_id="g1",
        description="Dinner",
        total_amount=90.0,
        paid_by="u1",
        split_type=SplitType.EQUAL,
        splits=splits,
    )

    # Assert splits are calculated equally
    assert expense.splits[0].amount == 30.0
    assert expense.splits[1].amount == 30.0
    assert expense.splits[2].amount == 30.0

    balances = service.get_balances("g1")
    # u1 paid 90, owes 30 -> net +60
    # u2 paid 0, owes 30 -> net -30
    # u3 paid 0, owes 30 -> net -30
    assert balances["u1"] == 60.0
    assert balances["u2"] == -30.0
    assert balances["u3"] == -30.0


def test_exact_split_success(splitwise_setup: SplitwiseService) -> None:
    service = splitwise_setup

    splits = [
        Split(user_id="u1", value=50.0),
        Split(user_id="u2", value=30.0),
        Split(user_id="u3", value=20.0),
    ]

    expense = service.add_expense(
        group_id="g1",
        description="Flight tickets",
        total_amount=100.0,
        paid_by="u2",
        split_type=SplitType.EXACT,
        splits=splits,
    )

    assert expense.splits[0].amount == 50.0
    assert expense.splits[1].amount == 30.0
    assert expense.splits[2].amount == 20.0


def test_exact_split_fail(splitwise_setup: SplitwiseService) -> None:
    service = splitwise_setup

    # Splits sum to 90, but total is 100
    splits = [
        Split(user_id="u1", value=40.0),
        Split(user_id="u2", value=30.0),
        Split(user_id="u3", value=20.0),
    ]

    with pytest.raises(ValueError, match="Exact split sum does not match"):
        service.add_expense(
            group_id="g1",
            description="Failed Tickets",
            total_amount=100.0,
            paid_by="u2",
            split_type=SplitType.EXACT,
            splits=splits,
        )


def test_percent_split_success(splitwise_setup: SplitwiseService) -> None:
    service = splitwise_setup

    splits = [
        Split(user_id="u1", value=50.0),
        Split(user_id="u2", value=30.0),
        Split(user_id="u3", value=20.0),
    ]

    expense = service.add_expense(
        group_id="g1",
        description="Airbnb",
        total_amount=250.0,
        paid_by="u1",
        split_type=SplitType.PERCENT,
        splits=splits,
    )

    assert expense.splits[0].amount == 125.0
    assert expense.splits[1].amount == 75.0
    assert expense.splits[2].amount == 50.0


def test_debt_simplification(splitwise_setup: SplitwiseService) -> None:
    service = splitwise_setup

    # Expense 1: u1 paid 300 for housing, split equally
    service.add_expense(
        group_id="g1",
        description="Housing",
        total_amount=300.0,
        paid_by="u1",
        split_type=SplitType.EQUAL,
        splits=[Split(user_id="u1"), Split(user_id="u2"), Split(user_id="u3")],
    )

    # Balances now: u1 (+200), u2 (-100), u3 (-100)

    # Expense 2: u2 paid 150 for Food, split equally
    service.add_expense(
        group_id="g1",
        description="Food",
        total_amount=150.0,
        paid_by="u2",
        split_type=SplitType.EQUAL,
        splits=[Split(user_id="u1"), Split(user_id="u2"), Split(user_id="u3")],
    )

    # Expense 2 splits: 50 each
    # Balances:
    # u1: +200 - 50 = +150
    # u2: -100 + 100 = 0
    # u3: -100 - 50 = -150

    balances = service.get_balances("g1")
    assert balances["u1"] == 150.0
    assert balances["u2"] == 0.0
    assert balances["u3"] == -150.0

    transactions = service.simplify_debts("g1")
    # Debt simplification: u3 should pay u1 $150 directly, and u2 is uninvolved!
    assert len(transactions) == 1
    assert transactions[0]["from_user"] == "u3"
    assert transactions[0]["to_user"] == "u1"
    assert transactions[0]["amount"] == 150.0
