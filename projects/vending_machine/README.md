# LLD Project: Vending Machine System

A Low-Level Design of a standard **Vending Machine System** using the **State Design Pattern** in Python, wrapped in a FastAPI web interface.

---

## 1. System Requirements

1. **State Machine Transitions**: Implement a clean state machine handling:
   - **IdleState**: Initial state, waiting for coin insertion.
   - **ReadyState**: Coin inserted, waiting for product selection or additional coins.
   - **SelectProductState**: Product selected, checking price vs balance, dispensing.
   - **DispenseState**: Item dispensed, calculating refund/change, returning to IdleState.
2. **Product Inventory**: Track product items (Soda, Chips, Candy) with code, price, and inventory count.
3. **Coin Handling**: Accept physical denominations (Nickels, Dimes, Quarters, Dollars).
4. **Refund/Cancel**: Allow users to cancel at any time, returning inserted money.
5. **FastAPI Web API**: Web interface simulating coin insertion, selection, cancelation, and dispensing.

---

## 2. Design Patterns Used

### State Pattern
The State Pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class. Instead of managing state using long `if-else` conditionals inside the context, we delegate behaviors to concrete `VendingMachineState` subclasses.

```mermaid
stateDiagram-v2
    [*] --> IdleState
    IdleState --> ReadyState : insert_coin()
    ReadyState --> ReadyState : insert_coin()
    ReadyState --> SelectProductState : select_product()
    ReadyState --> IdleState : refund() / cancel()
    SelectProductState --> DispenseState : check_balance() >= price
    SelectProductState --> ReadyState : check_balance() < price (insufficient funds)
    DispenseState --> IdleState : dispense() & return_change()
```

### UML Class Diagram

```mermaid
classDiagram
    direction TB
    class VendingMachine {
        -state: VendingMachineState
        -inventory: Inventory
        -balance: float
        -selected_product_code: str
        +set_state(state: VendingMachineState) void
        +insert_coin(coin: Coin) void
        +select_product(code: str) void
        +press_refund_button() List[Coin]
        +dispense_item() Item
    }
    class VendingMachineState {
        <<interface>>
        +insert_coin(machine: VendingMachine, coin: Coin) void
        +select_product(machine: VendingMachine, code: str) void
        +refund(machine: VendingMachine) List[Coin]
        +dispense(machine: VendingMachine) Item
    }
    class IdleState {
    }
    class ReadyState {
    }
    class SelectProductState {
    }
    class DispenseState {
    }

    VendingMachineState <|-- IdleState
    VendingMachineState <|-- ReadyState
    VendingMachineState <|-- SelectProductState
    VendingMachineState <|-- DispenseState
    VendingMachine "1" *-- "1" VendingMachineState
```
