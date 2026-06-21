import uuid
from typing import Any, Dict, List, Tuple

from .models import Expense, ExpenseGroup, Split, SplitType, User
from .strategies import EqualSplitStrategy, ExactSplitStrategy, PercentSplitStrategy, SplitStrategy


class SplitwiseService:
    def __init__(self) -> None:
        self.users: Dict[str, User] = {}
        self.groups: Dict[str, ExpenseGroup] = {}

        # Strategies mapping
        self.strategies: Dict[SplitType, SplitStrategy] = {
            SplitType.EQUAL: EqualSplitStrategy(),
            SplitType.EXACT: ExactSplitStrategy(),
            SplitType.PERCENT: PercentSplitStrategy(),
        }

    def add_user(self, user_id: str, name: str, email: str) -> User:
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists.")
        user = User(user_id=user_id, name=name, email=email)
        self.users[user_id] = user
        return user

    def create_group(self, group_id: str, name: str) -> ExpenseGroup:
        if group_id in self.groups:
            raise ValueError(f"Group with ID {group_id} already exists.")
        group = ExpenseGroup(group_id=group_id, name=name)
        self.groups[group_id] = group
        return group

    def add_user_to_group(self, group_id: str, user_id: str) -> None:
        if group_id not in self.groups:
            raise KeyError(f"Group {group_id} not found.")
        if user_id not in self.users:
            raise KeyError(f"User {user_id} not found.")

        group = self.groups[group_id]
        if user_id not in group.members:
            group.members.append(user_id)

    def add_expense(
        self,
        group_id: str,
        description: str,
        total_amount: float,
        paid_by: str,
        split_type: SplitType,
        splits: List[Split],
    ) -> Expense:
        if group_id not in self.groups:
            raise KeyError(f"Group {group_id} not found.")
        if paid_by not in self.users:
            raise KeyError(f"User paid_by {paid_by} not found.")

        group = self.groups[group_id]

        # Verify all split users are group members
        for split in splits:
            if split.user_id not in group.members:
                raise ValueError(
                    f"User {split.user_id} in split is not a member of group {group_id}."
                )

        # Calculate split amounts based on selected strategy
        strategy = self.strategies.get(split_type)
        if not strategy:
            raise ValueError(f"Unsupported split type: {split_type}")

        strategy.calculate_amounts(splits, total_amount)

        expense_id = str(uuid.uuid4())[:8]
        expense = Expense(
            expense_id=expense_id,
            description=description,
            total_amount=total_amount,
            paid_by=paid_by,
            split_type=split_type,
            splits=splits,
        )

        group.expenses.append(expense)
        return expense

    def get_balances(self, group_id: str) -> Dict[str, float]:
        """
        Calculates raw balances of all members in the group.
        Positive value: Owed money (is a creditor)
        Negative value: Owes money (is a debtor)
        """
        if group_id not in self.groups:
            raise KeyError(f"Group {group_id} not found.")

        group = self.groups[group_id]
        balances = {member_id: 0.0 for member_id in group.members}

        for expense in group.expenses:
            # The person who paid gets credit
            balances[expense.paid_by] += expense.total_amount
            # Each participant gets debited their share
            for split in expense.splits:
                balances[split.user_id] -= split.amount

        # Round balances to 2 decimal places
        return {uid: round(bal, 2) for uid, bal in balances.items()}

    def simplify_debts(self, group_id: str) -> List[Dict[str, Any]]:
        """
        Greedy Min-Flow Cash Flow algorithm to simplify debts.
        Returns a list of transactions needed to settle all debts in the group.
        """
        balances = self.get_balances(group_id)

        # Split into debtors (negative) and creditors (positive)
        debtors: List[Tuple[str, float]] = []
        creditors: List[Tuple[str, float]] = []

        for user_id, bal in balances.items():
            if bal < -0.01:
                debtors.append((user_id, bal))
            elif bal > 0.01:
                creditors.append((user_id, bal))

        # Sort debtors ascending (most negative first)
        # Sort creditors descending (most positive first)
        debtors.sort(key=lambda x: x[1])
        creditors.sort(key=lambda x: x[1], reverse=True)

        transactions = []

        debt_idx = 0
        cred_idx = 0

        while debt_idx < len(debtors) and cred_idx < len(creditors):
            debtor_id, debtor_bal = debtors[debt_idx]
            creditor_id, creditor_bal = creditors[cred_idx]

            # Find the minimum transaction amount to clear one of the balances
            amount_to_settle = min(-debtor_bal, creditor_bal)
            amount_to_settle = round(amount_to_settle, 2)

            transactions.append(
                {
                    "from_user": debtor_id,
                    "to_user": creditor_id,
                    "amount": amount_to_settle,
                }
            )

            # Adjust balances
            new_debtor_bal = round(debtor_bal + amount_to_settle, 2)
            new_creditor_bal = round(creditor_bal - amount_to_settle, 2)

            # Update values and move pointers
            if abs(new_debtor_bal) < 0.01:
                debt_idx += 1
            else:
                debtors[debt_idx] = (debtor_id, new_debtor_bal)

            if abs(new_creditor_bal) < 0.01:
                cred_idx += 1
            else:
                creditors[cred_idx] = (creditor_id, new_creditor_bal)

        return transactions
