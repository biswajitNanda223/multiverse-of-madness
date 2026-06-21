from abc import ABC, abstractmethod
from typing import List, Optional


class Command(ABC):
    """The Command interface declares a method for executing a command."""

    @abstractmethod
    def execute(self) -> str:
        """Executes the command logic."""
        pass


class SimpleCommand(Command):
    """Simple Command containing self-contained logic without a Receiver."""

    def __init__(self, payload: str) -> None:
        """Initializes a SimpleCommand.

        Args:
            payload: Data to be printed/processed.
        """
        self._payload = payload

    def execute(self) -> str:
        return f"SimpleCommand: Printing ({self._payload})"


class Receiver:
    """The Receiver containing the actual business logic executed by complex commands."""

    def do_something(self, a: str) -> str:
        return f"Receiver: Working on {a}"

    def do_something_else(self, b: str) -> str:
        return f"Receiver: Working on {b}"


class ComplexCommand(Command):
    """A Command that delegates operations to a Receiver."""

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """Initializes a ComplexCommand.

        Args:
            receiver: The business logic receiver.
            a: Parameter for the first receiver operation.
            b: Parameter for the second receiver operation.
        """
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> str:
        res1 = self._receiver.do_something(self._a)
        res2 = self._receiver.do_something_else(self._b)
        return f"ComplexCommand: {res1} and {res2}"


class Invoker:
    """The Invoker triggers command execution at custom moments or events."""

    def __init__(self) -> None:
        self._on_start: Optional[Command] = None
        self._on_finish: Optional[Command] = None

    def set_on_start(self, command: Command) -> None:
        """Sets command triggered at start of workflow."""
        self._on_start = command

    def set_on_finish(self, command: Command) -> None:
        """Sets command triggered at end of workflow."""
        self._on_finish = command

    def execute_workflow(self) -> List[str]:
        """Runs the main workflow executing commands at appropriate stages."""
        results = []
        if self._on_start:
            results.append(self._on_start.execute())
        results.append("Invoker: Processing core business task.")
        if self._on_finish:
            results.append(self._on_finish.execute())
        return results
