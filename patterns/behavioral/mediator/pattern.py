from abc import ABC, abstractmethod
from typing import Optional


class Mediator(ABC):
    """The Mediator interface declaring communication notification callback."""

    @abstractmethod
    def notify(self, sender: object, event: str) -> str:
        """Notifies the mediator of an event from a colleague component."""
        pass


class BaseComponent:
    """Colleague component that communicates only via mediator."""

    def __init__(self, mediator: Optional[Mediator] = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Optional[Mediator]:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class Button(BaseComponent):
    """Concrete Colleague: Button."""

    def click(self) -> str:
        """Simulates clicking the button."""
        res = "Button clicked."
        if self._mediator:
            mediator_res = self._mediator.notify(self, "click")
            return f"{res} {mediator_res}"
        return res


class TextBox(BaseComponent):
    """Concrete Colleague: TextBox."""

    def __init__(self, mediator: Optional[Mediator] = None) -> None:
        super().__init__(mediator)
        self.text = ""

    def set_text(self, text: str) -> str:
        """Sets text and notifies the mediator of changes."""
        self.text = text
        res = f"TextBox set to '{text}'."
        if self._mediator:
            mediator_res = self._mediator.notify(self, "change")
            return f"{res} {mediator_res}"
        return res


class AuthenticationMediator(Mediator):
    """Concrete Mediator coordinating interactions between Button and TextBox components."""

    def __init__(self, button: Button, textbox: TextBox) -> None:
        self._button = button
        self._button.mediator = self
        self._textbox = textbox
        self._textbox.mediator = self

    def notify(self, sender: object, event: str) -> str:
        if sender is self._button and event == "click":
            if not self._textbox.text:
                return "Mediator: Validation failed. Textbox is empty."
            return f"Mediator: Logging in user with input '{self._textbox.text}'."
        elif sender is self._textbox and event == "change":
            return "Mediator: Input changed. Validation status reset."
        return "Mediator: Unknown event."
