import pytest

from .models import Coin, Item
from .service import VendingMachine


@pytest.fixture
def machine_setup() -> VendingMachine:
    machine = VendingMachine()
    # Add products
    soda = Item(name="Soda", price=1.50, code="A1")
    chips = Item(name="Chips", price=1.00, code="A2")
    machine.inventory.add_product(soda, 2)
    machine.inventory.add_product(chips, 0)  # out of stock
    return machine


def test_initial_state_is_idle(machine_setup: VendingMachine) -> None:
    machine = machine_setup
    assert machine.state.__class__.__name__ == "IdleState"
    assert machine.balance == 0.0


def test_insert_coin_transitions_to_ready(machine_setup: VendingMachine) -> None:
    machine = machine_setup
    machine.insert_coin(Coin.DOLLAR)

    assert machine.state.__class__.__name__ == "ReadyState"
    assert machine.balance == 1.00


def test_select_product_insufficient_balance(machine_setup: VendingMachine) -> None:
    machine = machine_setup
    machine.insert_coin(Coin.DOLLAR)  # total $1.00, Soda is $1.50

    machine.select_product("A1")
    with pytest.raises(ValueError, match="Insufficient balance"):
        machine.check_balance_and_dispense()

    # State should remain ReadyState to insert more coins
    assert machine.state.__class__.__name__ == "ReadyState"


def test_select_product_out_of_stock(machine_setup: VendingMachine) -> None:
    machine = machine_setup
    machine.insert_coin(Coin.DOLLAR)

    with pytest.raises(ValueError, match="out of stock"):
        machine.select_product("A2")


def test_dispense_and_change_return(machine_setup: VendingMachine) -> None:
    machine = machine_setup
    # Insert $1.75
    machine.insert_coin(Coin.DOLLAR)
    machine.insert_coin(Coin.QUARTER)
    machine.insert_coin(Coin.QUARTER)
    machine.insert_coin(Coin.QUARTER)  # balance $1.75

    assert machine.balance == 1.75

    # Select Soda ($1.50)
    # The select_product method automatically triggers dispense_item() if state transitions
    machine.select_product("A1")

    item, change = machine.check_balance_and_dispense()

    assert item.name == "Soda"
    assert change == 0.25
    assert machine.balance == 0.0
    assert machine.state.__class__.__name__ == "IdleState"
    assert machine.inventory.stock["A1"] == 1  # decremented


def test_refund_success(machine_setup: VendingMachine) -> None:
    machine = machine_setup
    machine.insert_coin(Coin.DOLLAR)
    machine.insert_coin(Coin.QUARTER)

    refunded = machine.press_refund_button()

    assert len(refunded) == 2
    assert Coin.DOLLAR in refunded
    assert Coin.QUARTER in refunded
    assert machine.balance == 0.0
    assert machine.state.__class__.__name__ == "IdleState"
