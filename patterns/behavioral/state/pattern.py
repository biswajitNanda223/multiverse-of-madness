from abc import ABC, abstractmethod
from typing import Optional


class DocumentState(ABC):
    """Abstract State class defining operations document states must implement."""

    def __init__(self) -> None:
        self._document: Optional["Document"] = None

    @property
    def document(self) -> "Document":
        """Gets the owner document context."""
        if self._document is None:
            raise ValueError("Document context is not initialized.")
        return self._document

    @document.setter
    def document(self, doc: "Document") -> None:
        """Sets the owner document context."""
        self._document = doc

    @abstractmethod
    def publish(self) -> str:
        """Publishes/advances state of the document."""
        pass

    @abstractmethod
    def render(self) -> str:
        """Renders document view according to state."""
        pass


class Document:
    """The Context class that maintains a reference to the current state."""

    def __init__(self, state: DocumentState) -> None:
        """Initializes the document with an initial state."""
        self._state: DocumentState = state
        self.transition_to(state)

    def transition_to(self, state: DocumentState) -> None:
        """Transitions document context to a new state."""
        self._state = state
        self._state.document = self

    def publish(self) -> str:
        """Invokes publish on current state."""
        return self._state.publish()

    def render(self) -> str:
        """Invokes render on current state."""
        return self._state.render()


class DraftState(DocumentState):
    """Concrete State: Draft."""

    def publish(self) -> str:
        self.document.transition_to(ModerationState())
        return "Draft: Moved document to Moderation."

    def render(self) -> str:
        return "Draft: Rendering editor workspace views."


class ModerationState(DocumentState):
    """Concrete State: Moderation."""

    def publish(self) -> str:
        self.document.transition_to(PublishedState())
        return "Moderation: Moved document to Published."

    def render(self) -> str:
        return "Moderation: Rendering admin review workspace."


class PublishedState(DocumentState):
    """Concrete State: Published."""

    def publish(self) -> str:
        return "Published: Document is already published."

    def render(self) -> str:
        return "Published: Rendering public reading views."
