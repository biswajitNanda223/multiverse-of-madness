from typing import List, Optional, Tuple

from .models import Coin, Inventory, Item
from .states import IdleState, VendingMachineState


class VendingMachine:
    def __init__(self) -> None:
        self.inventory: Inventory = Inventory()
        self.balance: float = 0.0
        self.selected_product_code: Optional[str] = None
        # Initial State: Idle
        self.state: VendingMachineState = IdleState()

    def set_state(self, state: VendingMachineState) -> None:
        self.state = state

    def insert_coin(self, coin: Coin) -> None:
        self.state.insert_coin(self, coin)

    def select_product(self, code: str) -> None:
        self.state.select_product(self, code)

    def press_refund_button(self) -> List[Coin]:
        return self.state.refund(self)

    def check_balance_and_dispense(self) -> Tuple[Item, float]:
        """Triggered from ReadyState/SelectProductState to evaluate balance."""
        return self.state.dispense(self)

    def dispense_item(self) -> Tuple[Item, float]:
        """Internal call to run actual dispense state logic."""
        return self.state.dispense(self)

    def return_change(self, amount: float) -> List[Coin]:
        """Greedy algorithm to return change in coins."""
        change_coins: List[Coin] = []
        amount = round(amount, 2)

        # Available denominations sorted descending
        denominations = [Coin.DOLLAR, Coin.QUARTER, Coin.DIME, Coin.NICKEL]

        for denom in denominations:
            while (
                amount >= denom.value - 0.001
            ):  # check with tolerance for floating precision
                change_coins.append(denom)
                amount = round(amount - denom.value, 2)

        return change_coins
