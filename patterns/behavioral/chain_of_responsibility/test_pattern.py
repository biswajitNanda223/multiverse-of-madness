from patterns.behavioral.chain_of_responsibility.pattern import (
    DogHandler,
    MonkeyHandler,
    SquirrelHandler,
)


def test_chain_of_responsibility_handling() -> None:
    """Verifies correct execution of requests through the chain."""
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    # Link the chain
    monkey.set_next(squirrel).set_next(dog)

    # Monkey handles banana
    assert monkey.handle("Banana") == "Monkey: I will eat the Banana."

    # Squirrel handles nut
    assert monkey.handle("Nut") == "Squirrel: I will eat the Nut."

    # Dog handles meatball
    assert monkey.handle("Meatball") == "Dog: I will eat the Meatball."

    # Unhandled requests bubble to the end and return None
    assert monkey.handle("Cabbage") is None
