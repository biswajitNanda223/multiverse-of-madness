from abc import ABC, abstractmethod
from typing import List, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from .service import VendingMachine

from .models import Coin, Item


class VendingMachineState(ABC):
    @abstractmethod
    def insert_coin(self, machine: "VendingMachine", coin: Coin) -> None:
        """Handle inserting a coin."""
        pass

    @abstractmethod
    def select_product(self, machine: "VendingMachine", code: str) -> None:
        """Handle product selection."""
        pass

    @abstractmethod
    def refund(self, machine: "VendingMachine") -> List[Coin]:
        """Cancel transaction and refund current balance."""
        pass

    @abstractmethod
    def dispense(self, machine: "VendingMachine") -> Tuple[Item, float]:
        """Dispense product and calculate refund change."""
        pass


class IdleState(VendingMachineState):
    def insert_coin(self, machine: "VendingMachine", coin: Coin) -> None:
        machine.balance += coin.value
        print(
            f"Coin inserted: {coin.name} (${coin.value}). Current balance: ${machine.balance:.2f}"
        )
        # Transition to ReadyState
        from .states import ReadyState

        machine.set_state(ReadyState())

    def select_product(self, machine: "VendingMachine", code: str) -> None:
        raise ValueError("Please insert coins first.")

    def refund(self, machine: "VendingMachine") -> List[Coin]:
        raise ValueError("No coins to refund. Machine is idle.")

    def dispense(self, machine: "VendingMachine") -> Tuple[Item, float]:
        raise ValueError("Insert coins and select a product first.")


class ReadyState(VendingMachineState):
    def insert_coin(self, machine: "VendingMachine", coin: Coin) -> None:
        machine.balance += coin.value
        print(
            f"Coin inserted: {coin.name} (${coin.value}). Current balance: ${machine.balance:.2f}"
        )

    def select_product(self, machine: "VendingMachine", code: str) -> None:
        item = machine.inventory.get_product(code)
        if not item:
            raise ValueError(f"Product code {code} not found.")

        if not machine.inventory.is_available(code):
            raise ValueError(f"Product {item.name} is out of stock.")

        machine.selected_product_code = code

        # Transition to SelectProductState
        from .states import SelectProductState

        machine.set_state(SelectProductState())

    def refund(self, machine: "VendingMachine") -> List[Coin]:
        refund_coins = machine.return_change(machine.balance)
        machine.balance = 0.0
        machine.selected_product_code = None
        from .states import IdleState

        machine.set_state(IdleState())
        return refund_coins

    def dispense(self, machine: "VendingMachine") -> Tuple[Item, float]:
        raise ValueError("Select a product first.")


class SelectProductState(VendingMachineState):
    def insert_coin(self, machine: "VendingMachine", coin: Coin) -> None:
        raise ValueError("Processing product selection. Cannot insert coins now.")

    def select_product(self, machine: "VendingMachine", code: str) -> None:
        raise ValueError("Product already selected. Processing payment.")

    def refund(self, machine: "VendingMachine") -> List[Coin]:
        refund_coins = machine.return_change(machine.balance)
        machine.balance = 0.0
        machine.selected_product_code = None
        from .states import IdleState

        machine.set_state(IdleState())
        return refund_coins

    def dispense(self, machine: "VendingMachine") -> Tuple[Item, float]:
        code = machine.selected_product_code
        if not code:
            raise ValueError("No product selected.")

        item = machine.inventory.get_product(code)
        if not item:
            raise ValueError("Product not found.")

        if machine.balance < item.price:
            # Revert to ReadyState to allow inserting more coins
            from .states import ReadyState

            machine.set_state(ReadyState())
            raise ValueError(
                f"Insufficient balance. Product price: ${item.price:.2f}, "
                f"balance: ${machine.balance:.2f}"
            )

        # Transition to DispenseState
        from .states import DispenseState

        machine.set_state(DispenseState())
        return machine.dispense_item()


class DispenseState(VendingMachineState):
    def insert_coin(self, machine: "VendingMachine", coin: Coin) -> None:
        raise ValueError("Dispensing item. Cannot insert coins.")

    def select_product(self, machine: "VendingMachine", code: str) -> None:
        raise ValueError("Dispensing item. Cannot select another product.")

    def refund(self, machine: "VendingMachine") -> List[Coin]:
        raise ValueError("Dispensing item. Cannot cancel now.")

    def dispense(self, machine: "VendingMachine") -> Tuple[Item, float]:
        code = machine.selected_product_code
        if not code:
            raise ValueError("No product selected.")

        item = machine.inventory.get_product(code)
        if not item:
            raise ValueError("Product not found.")

        # Dispense item (decrement inventory stock)
        machine.inventory.decrement_stock(code)

        # Calculate change
        change = round(machine.balance - item.price, 2)
        machine.balance = 0.0
        machine.selected_product_code = None

        # Go back to IdleState
        from .states import IdleState

        machine.set_state(IdleState())

        return item, change
