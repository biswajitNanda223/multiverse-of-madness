from datetime import datetime
from typing import List


class Memento:
    """The Memento class containing the saved state snapshot and metadata."""

    def __init__(self, state: str) -> None:
        """Initializes a Memento snapshot.

        Args:
            state: The text state of the originator.
        """
        self._state = state
        self._date = str(datetime.now())

    def get_state(self) -> str:
        """Retrieves the encapsulated state (Originator only)."""
        return self._state

    def get_name(self) -> str:
        """Gets a string preview name for caretaker history logs."""
        return f"{self._date} / ({self._state[:9]}...)"

    def get_date(self) -> str:
        """Gets snapshot creation timestamp."""
        return self._date


class Originator:
    """The Originator whose internal state is saved and restored."""

    def __init__(self, state: str) -> None:
        self._state = state

    def set_state(self, state: str) -> None:
        """Updates the internal state."""
        self._state = state

    def get_state(self) -> str:
        """Gets the current internal state."""
        return self._state

    def save(self) -> Memento:
        """Saves current state inside a new Memento instance."""
        return Memento(self._state)

    def restore(self, memento: Memento) -> None:
        """Restores internal state from a Memento instance."""
        self._state = memento.get_state()


class Caretaker:
    """The Caretaker managing memento storage histories, coordinating undos."""

    def __init__(self, originator: Originator) -> None:
        """Initializes the Caretaker.

        Args:
            originator: The Originator to manage.
        """
        self._mementos: List[Memento] = []
        self._originator = originator

    def backup(self) -> None:
        """Saves current state of originator to history."""
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        """Restores the originator to the last saved state."""
        if not self._mementos:
            return
        memento = self._mementos.pop()
        self._originator.restore(memento)

    def get_history_length(self) -> int:
        """Returns the size of the history stack."""
        return len(self._mementos)
