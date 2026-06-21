from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    """The Handler interface declares a method for building the chain of handlers.

    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: "Handler") -> "Handler":
        """Sets the next handler in the chain."""
        pass

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        """Handles the request or passes it to the next handler."""
        pass


class AbstractHandler(Handler):
    """The default chaining behavior."""

    def __init__(self) -> None:
        self._next_handler: Optional[Handler] = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: str) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class MonkeyHandler(AbstractHandler):
    """Concrete Handler that processes bananas."""

    def handle(self, request: str) -> Optional[str]:
        if request == "Banana":
            return "Monkey: I will eat the Banana."
        return super().handle(request)


class SquirrelHandler(AbstractHandler):
    """Concrete Handler that processes nuts."""

    def handle(self, request: str) -> Optional[str]:
        if request == "Nut":
            return "Squirrel: I will eat the Nut."
        return super().handle(request)


class DogHandler(AbstractHandler):
    """Concrete Handler that processes meatballs."""

    def handle(self, request: str) -> Optional[str]:
        if request == "Meatball":
            return "Dog: I will eat the Meatball."
        return super().handle(request)
