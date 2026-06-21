from abc import ABC, abstractmethod


class Notifier(ABC):
    """The Component interface defining notification operations."""

    @abstractmethod
    def send(self, message: str) -> str:
        """Sends a notification message."""
        pass


class EmailNotifier(Notifier):
    """The Concrete Component providing basic email notifications."""

    def send(self, message: str) -> str:
        return f"Sending Email: {message}"


class BaseNotifierDecorator(Notifier):
    """The Base Decorator wrapping a Notifier component."""

    def __init__(self, wrappee: Notifier) -> None:
        """Initializes the decorator with a component to wrap.

        Args:
            wrappee: The Notifier instance being wrapped.
        """
        self._wrappee = wrappee

    def send(self, message: str) -> str:
        """Delegates the send operation to the wrapped component."""
        return self._wrappee.send(message)


class SMSDecorator(BaseNotifierDecorator):
    """Concrete Decorator adding SMS capabilities."""

    def send(self, message: str) -> str:
        parent_notifications = super().send(message)
        return f"{parent_notifications} and Sending SMS: {message}"


class SlackDecorator(BaseNotifierDecorator):
    """Concrete Decorator adding Slack message capabilities."""

    def send(self, message: str) -> str:
        parent_notifications = super().send(message)
        return f"{parent_notifications} and Sending Slack: {message}"
