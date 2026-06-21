from patterns.behavioral.interpreter.pattern import (
    AddExpression,
    NumberExpression,
    SubtractExpression,
)


def test_terminal_expressions() -> None:
    """Verifies that terminal number expressions evaluate values and variables."""
    context = {"x": 10, "y": -5}

    expr_x = NumberExpression("x")
    expr_y = NumberExpression("y")
    expr_const = NumberExpression("25")
    expr_missing = NumberExpression("z")

    assert expr_x.interpret(context) == 10
    assert expr_y.interpret(context) == -5
    assert expr_const.interpret(context) == 25
    assert expr_missing.interpret(context) == 0


def test_math_operations() -> None:
    """Verifies that non-terminal expressions perform addition and subtraction."""
    context = {"a": 40, "b": 10, "c": 5}

    # a + b
    expr_add = AddExpression(NumberExpression("a"), NumberExpression("b"))
    assert expr_add.interpret(context) == 50

    # a - b
    expr_sub = SubtractExpression(NumberExpression("a"), NumberExpression("b"))
    assert expr_sub.interpret(context) == 30

    # (a + b) - c  =>  (40 + 10) - 5 = 45
    expr_nested = SubtractExpression(expr_add, NumberExpression("c"))
    assert expr_nested.interpret(context) == 45
