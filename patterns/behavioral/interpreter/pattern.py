from abc import ABC, abstractmethod
from typing import Dict


class Expression(ABC):
    """The Abstract Expression defines the interface for evaluating expressions in a context."""

    @abstractmethod
    def interpret(self, context: Dict[str, int]) -> int:
        """Evaluates the expression with the given context variables."""
        pass


class NumberExpression(Expression):
    """Terminal Expression that resolves a numeric value or evaluates a variable from context."""

    def __init__(self, value_or_var: str) -> None:
        """Initializes NumberExpression.

        Args:
            value_or_var: The name of the variable or a string digit.
        """
        self.value_or_var = value_or_var

    def interpret(self, context: Dict[str, int]) -> int:
        if self.value_or_var.isdigit() or (
            self.value_or_var.startswith("-") and self.value_or_var[1:].isdigit()
        ):
            return int(self.value_or_var)
        return context.get(self.value_or_var, 0)


class AddExpression(Expression):
    """Non-terminal Expression representing addition of two sub-expressions."""

    def __init__(self, left: Expression, right: Expression) -> None:
        """Initializes AddExpression.

        Args:
            left: The left operand expression.
            right: The right operand expression.
        """
        self.left = left
        self.right = right

    def interpret(self, context: Dict[str, int]) -> int:
        return self.left.interpret(context) + self.right.interpret(context)


class SubtractExpression(Expression):
    """Non-terminal Expression representing subtraction of two sub-expressions."""

    def __init__(self, left: Expression, right: Expression) -> None:
        """Initializes SubtractExpression.

        Args:
            left: The left operand expression.
            right: The right operand expression.
        """
        self.left = left
        self.right = right

    def interpret(self, context: Dict[str, int]) -> int:
        return self.left.interpret(context) - self.right.interpret(context)
