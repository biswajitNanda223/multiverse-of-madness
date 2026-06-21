from typing import Any, Dict, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .models import Coin, Item
from .service import VendingMachine

app = FastAPI(
    title="Vending Machine LLD API",
    description="Low-Level Design implementation of a Vending Machine using the State Pattern.",
    version="1.0.0",
)

# Instantiate Vending Machine context
vending_machine = VendingMachine()


# Request/Response Schemas
class PopulateInventoryRequest(BaseModel):
    items: List[Dict[str, Any]] = Field(
        default=[
            {"name": "Soda", "price": 1.50, "code": "A1", "quantity": 5},
            {"name": "Chips", "price": 1.00, "code": "A2", "quantity": 3},
            {"name": "Candy", "price": 0.75, "code": "A3", "quantity": 10},
        ],
        description="List of items with quantity to load into the machine",
    )


class InsertCoinRequest(BaseModel):
    coin: float = Field(
        ...,
        description=(
            "Denomination of coin: 0.05 (NICKEL), 0.10 (DIME), " "0.25 (QUARTER), 1.00 (DOLLAR)"
        ),
    )


class SelectProductRequest(BaseModel):
    code: str = Field(..., description="Alphanumeric product key, e.g., 'A1'")


# Endpoints
@app.post("/inventory/init", tags=["Inventory Management"])
def initialize_inventory(request: PopulateInventoryRequest) -> Dict[str, str]:
    try:
        # Reset inventory
        from .models import Inventory

        vending_machine.inventory = Inventory()
        vending_machine.balance = 0.0
        vending_machine.selected_product_code = None
        from .states import IdleState

        vending_machine.set_state(IdleState())

        for item_data in request.items:
            item = Item(name=item_data["name"], price=item_data["price"], code=item_data["code"])
            vending_machine.inventory.add_product(item, item_data["quantity"])

        return {"status": "success", "message": "Inventory successfully initialized."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/insert-coin", tags=["Vending Machine Actions"])
def insert_coin(request: InsertCoinRequest) -> Dict[str, Any]:
    try:
        # Validate coin from float value
        try:
            coin_enum = Coin(request.coin)
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail=(
                    "Invalid coin value. Allowed: 0.05 (NICKEL), "
                    "0.10 (DIME), 0.25 (QUARTER), 1.00 (DOLLAR)"
                ),
            )

        vending_machine.insert_coin(coin_enum)
        return {
            "status": "success",
            "current_balance": vending_machine.balance,
            "machine_state": vending_machine.state.__class__.__name__,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/select-product", tags=["Vending Machine Actions"])
def select_product(request: SelectProductRequest) -> Dict[str, Any]:
    try:
        # Select product (might trigger dispense if balance is sufficient)
        vending_machine.select_product(request.code)

        # If it was successful, we would have transitioned to IdleState or SelectProductState
        # Let's handle check and response
        return {
            "status": "success",
            "message": "Product selection processed.",
            "current_state": vending_machine.state.__class__.__name__,
        }
    except ValueError as e:
        # If we failed (e.g. insufficient funds, out of stock, or need coin first)
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/dispense", tags=["Vending Machine Actions"])
def dispense_item() -> Dict[str, Any]:
    try:
        item, change = vending_machine.check_balance_and_dispense()
        # Format change coins list
        change_list = [c.name for c in vending_machine.return_change(change)]
        return {
            "status": "success",
            "message": "Item dispensed successfully.",
            "dispensed_item": item,
            "change_returned_amount": change,
            "change_coins": change_list,
            "machine_state": vending_machine.state.__class__.__name__,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/refund", tags=["Vending Machine Actions"])
def press_refund_button() -> Dict[str, Any]:
    try:
        refunded_coins = vending_machine.press_refund_button()
        refund_amount = sum(c.value for c in refunded_coins)
        return {
            "status": "success",
            "message": "Refund processed.",
            "refund_amount": refund_amount,
            "refund_coins": [c.name for c in refunded_coins],
            "machine_state": vending_machine.state.__class__.__name__,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/status", tags=["Monitoring"])
def get_vending_machine_status() -> Dict[str, Any]:
    stock_status = {}
    for code, item in vending_machine.inventory.products.items():
        stock_status[code] = {
            "name": item.name,
            "price": item.price,
            "quantity_available": vending_machine.inventory.stock.get(code, 0),
        }

    return {
        "machine_state": vending_machine.state.__class__.__name__,
        "current_balance": vending_machine.balance,
        "selected_product_code": vending_machine.selected_product_code,
        "inventory": stock_status,
    }
