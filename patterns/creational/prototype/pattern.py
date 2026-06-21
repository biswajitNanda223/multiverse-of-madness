import copy
from typing import Any, List


class Prototype:
    """Interface / Base class for Prototype that supports cloning.

    Subclasses inherit or override clone to return a deep copy.
    """

    def clone(self) -> Any:
        """Clones the prototype using a deep copy.

        Returns:
            A deep copy of the current instance.
        """
        return copy.deepcopy(self)


class ConcretePrototype(Prototype):
    """A concrete implementation of Prototype with list values and references."""

    def __init__(self, name: str, tags: List[str]) -> None:
        """Initializes the concrete prototype.

        Args:
            name: Name of the prototype.
            tags: A list of string tags.
        """
        self.name = name
        self.tags = tags
        self.circular_ref: Any = None

    def add_tag(self, tag: str) -> None:
        """Adds a tag to the tag list."""
        self.tags.append(tag)
