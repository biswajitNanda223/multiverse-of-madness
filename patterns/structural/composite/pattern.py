from abc import ABC, abstractmethod
from typing import List


class CatalogComponent(ABC):
    """The Component interface declares common operations for simple and complex components."""

    @abstractmethod
    def get_name(self) -> str:
        """Gets the name of the component."""
        pass

    @abstractmethod
    def get_price(self) -> float:
        """Gets the price of the component."""
        pass

    def add(self, component: "CatalogComponent") -> None:
        """Adds a child component (composite only)."""
        raise NotImplementedError("Cannot add to a leaf element.")

    def remove(self, component: "CatalogComponent") -> None:
        """Removes a child component (composite only)."""
        raise NotImplementedError("Cannot remove from a leaf element.")

    def is_composite(self) -> bool:
        """Checks if the component is composite."""
        return False


class Product(CatalogComponent):
    """The Leaf class representing individual product items that cannot have children."""

    def __init__(self, name: str, price: float) -> None:
        """Initializes a Product leaf.

        Args:
            name: The product name.
            price: The product price.
        """
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price


class Box(CatalogComponent):
    """The Composite class representing packages/boxes containing other items."""

    def __init__(self, name: str) -> None:
        """Initializes a Box composite.

        Args:
            name: The name of the box.
        """
        self.name = name
        self._children: List[CatalogComponent] = []

    def get_name(self) -> str:
        return self.name

    def add(self, component: CatalogComponent) -> None:
        self._children.append(component)

    def remove(self, component: CatalogComponent) -> None:
        self._children.remove(component)

    def is_composite(self) -> bool:
        return True

    def get_price(self) -> float:
        """Recursively aggregates the price of all components inside this Box."""
        total = 0.0
        for child in self._children:
            total += child.get_price()
        return total
