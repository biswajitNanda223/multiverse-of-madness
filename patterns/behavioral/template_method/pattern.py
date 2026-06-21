from abc import ABC, abstractmethod
from typing import List


class HouseBuilder(ABC):
    """The Abstract Class defining the Template Method."""

    def build_house(self) -> List[str]:
        """The Template Method defining the fixed skeleton sequence of house construction."""
        steps = []
        steps.append(self.build_foundation())
        steps.append(self.build_walls())
        steps.append(self.build_roof())
        steps.append(self.build_windows())

        # Optional Hook execution
        hook_res = self.add_decorations()
        if hook_res:
            steps.append(hook_res)
        return steps

    def build_foundation(self) -> str:
        """Concrete default step."""
        return "Foundation: Laying concrete foundation."

    @abstractmethod
    def build_walls(self) -> str:
        """Abstract step to be implemented by subclasses."""
        pass

    @abstractmethod
    def build_roof(self) -> str:
        """Abstract step to be implemented by subclasses."""
        pass

    def build_windows(self) -> str:
        """Concrete default step."""
        return "Windows: Installing glass windows."

    def add_decorations(self) -> str:
        """Hook method. Subclasses can override, but it is optional."""
        return ""


class WoodenHouse(HouseBuilder):
    """Concrete subclass building a wooden house."""

    def build_walls(self) -> str:
        return "Walls: Erecting wooden log walls."

    def build_roof(self) -> str:
        return "Roof: Installing wood shingle roof."


class BrickHouse(HouseBuilder):
    """Concrete subclass building a brick house and adding decorations."""

    def build_walls(self) -> str:
        return "Walls: Laying brick walls with mortar."

    def build_roof(self) -> str:
        return "Roof: Installing slate roof."

    def add_decorations(self) -> str:
        """Overridden optional hook."""
        return "Decorations: Painting walls and hanging a flag."
