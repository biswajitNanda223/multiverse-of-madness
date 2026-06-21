from typing import Dict, List


class TreeType:
    """The Flyweight class storing intrinsic (shared) state like name, color, and texture."""

    def __init__(self, name: str, color: str, texture: str) -> None:
        """Initializes the TreeType flyweight.

        Args:
            name: The type name (e.g., Oak).
            color: Leaf color (e.g., Green).
            texture: Bark texture (e.g., Rough).
        """
        self.name = name
        self.color = color
        self.texture = texture

    def display(self, x: int, y: int) -> str:
        """Renders the tree using extrinsic (unique) state (x, y)."""
        return f"Tree {self.name} ({self.color}/{self.texture}) at ({x}, {y})"


class TreeFactory:
    """The Flyweight Factory that caches and manages TreeType instances."""

    _tree_types: Dict[str, TreeType] = {}

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        """Gets an existing TreeType flyweight or creates one if not found.

        Args:
            name: Type name.
            color: Color.
            texture: Texture.

        Returns:
            A shared TreeType instance.
        """
        key = f"{name}_{color}_{texture}"
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
        return cls._tree_types[key]

    @classmethod
    def get_count(cls) -> int:
        """Gets total number of active flyweight instances in the factory cache."""
        return len(cls._tree_types)

    @classmethod
    def clear(cls) -> None:
        """Clears the flyweight cache registry."""
        cls._tree_types.clear()


class Tree:
    """The Context class holding extrinsic state (x, y) and referencing a Flyweight."""

    def __init__(self, x: int, y: int, tree_type: TreeType) -> None:
        """Initializes a Tree context.

        Args:
            x: X-coordinate.
            y: Y-coordinate.
            tree_type: The shared TreeType flyweight.
        """
        self.x = x
        self.y = y
        self.type = tree_type

    def draw(self) -> str:
        """Delegates drawing to the shared TreeType with extrinsic coordinates."""
        return self.type.display(self.x, self.y)


class Forest:
    """Client class coordinating tree creation and drawing."""

    def __init__(self) -> None:
        self.trees: List[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str) -> Tree:
        """Plants a tree by retrieving a flyweight and storing the context."""
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)
        return tree

    def draw(self) -> List[str]:
        """Draws all trees in the forest."""
        return [tree.draw() for tree in self.trees]
