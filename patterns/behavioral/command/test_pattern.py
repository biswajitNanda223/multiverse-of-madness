from patterns.behavioral.command.pattern import (
    ComplexCommand,
    Invoker,
    Receiver,
    SimpleCommand,
)


def test_simple_command() -> None:
    """Verifies SimpleCommand standalone execution."""
    cmd = SimpleCommand("hello payload")
    assert cmd.execute() == "SimpleCommand: Printing (hello payload)"


def test_complex_command() -> None:
    """Verifies ComplexCommand receiver integration."""
    receiver = Receiver()
    cmd = ComplexCommand(receiver, "Task A", "Task B")
    expected = (
        "ComplexCommand: Receiver: Working on Task A and Receiver: Working on Task B"
    )
    assert cmd.execute() == expected


def test_invoker_workflow() -> None:
    """Verifies that the Invoker coordinates start and end commands."""
    invoker = Invoker()
    receiver = Receiver()

    cmd_start = SimpleCommand("startup")
    cmd_finish = ComplexCommand(receiver, "write logs", "send email")

    invoker.set_on_start(cmd_start)
    invoker.set_on_finish(cmd_finish)

    workflow_results = invoker.execute_workflow()

    assert len(workflow_results) == 3
    assert workflow_results[0] == "SimpleCommand: Printing (startup)"
    assert workflow_results[1] == "Invoker: Processing core business task."
    assert (
        workflow_results[2]
        == "ComplexCommand: Receiver: Working on write logs and Receiver: Working on send email"
    )
