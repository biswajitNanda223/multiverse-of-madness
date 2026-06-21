from enum import Enum
from typing import Dict, Optional

from pydantic import BaseModel


class Coin(float, Enum):
    NICKEL = 0.05
    DIME = 0.10
    QUARTER = 0.25
    DOLLAR = 1.00


class Item(BaseModel):
    name: str
    price: float
    code: str


class Inventory:
    def __init__(self) -> None:
        self.products: Dict[str, Item] = {}
        self.stock: Dict[str, int] = {}

    def add_product(self, item: Item, quantity: int) -> None:
        self.products[item.code] = item
        self.stock[item.code] = self.stock.get(item.code, 0) + quantity

    def get_product(self, code: str) -> Optional[Item]:
        return self.products.get(code)

    def is_available(self, code: str) -> bool:
        return self.stock.get(code, 0) > 0

    def decrement_stock(self, code: str) -> None:
        if self.is_available(code):
            self.stock[code] -= 1
