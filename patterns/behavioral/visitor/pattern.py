from abc import ABC, abstractmethod


# Element Interface
class ShapeElement(ABC):
    """The Element interface declares an 'accept' method that takes a Visitor."""

    @abstractmethod
    def accept(self, visitor: "ShapeVisitor") -> str:
        """Accepts a visitor object."""
        pass


# Concrete Elements
class Dot(ShapeElement):
    """Concrete Element representing a Dot shape."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def accept(self, visitor: "ShapeVisitor") -> str:
        """Double dispatch redirecting execution to visitor.visit_dot."""
        return visitor.visit_dot(self)


class Circle(ShapeElement):
    """Concrete Element representing a Circle shape."""

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def accept(self, visitor: "ShapeVisitor") -> str:
        """Double dispatch redirecting execution to visitor.visit_circle."""
        return visitor.visit_circle(self)


# Visitor Interface
class ShapeVisitor(ABC):
    """The Visitor interface declaring visit operations for all concrete elements."""

    @abstractmethod
    def visit_dot(self, dot: Dot) -> str:
        """Visits a Dot element."""
        pass

    @abstractmethod
    def visit_circle(self, circle: Circle) -> str:
        """Visits a Circle element."""
        pass


# Concrete Visitors
class XMLExportVisitor(ShapeVisitor):
    """Concrete Visitor executing XML serialization."""

    def visit_dot(self, dot: Dot) -> str:
        return f'<dot x="{dot.x}" y="{dot.y}"/>'

    def visit_circle(self, circle: Circle) -> str:
        return f'<circle radius="{circle.radius}"/>'


class JSONExportVisitor(ShapeVisitor):
    """Concrete Visitor executing JSON serialization."""

    def visit_dot(self, dot: Dot) -> str:
        return f'{{"type": "dot", "x": {dot.x}, "y": {dot.y}}}'

    def visit_circle(self, circle: Circle) -> str:
        return f'{{"type": "circle", "radius": {circle.radius}}}'
