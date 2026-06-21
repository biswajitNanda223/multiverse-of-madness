from patterns.behavioral.memento.pattern import Caretaker, Originator


def test_memento_undo_redo() -> None:
    """Verifies that Caretaker correctly saves and restores Originator states."""
    originator = Originator("State #1")
    caretaker = Caretaker(originator)

    # Save State #1
    caretaker.backup()
    assert caretaker.get_history_length() == 1

    # Change to State #2 and Save
    originator.set_state("State #2")
    caretaker.backup()
    assert caretaker.get_history_length() == 2

    # Change to State #3 (Not Saved)
    originator.set_state("State #3")
    assert originator.get_state() == "State #3"

    # Undo 1: returns to State #2
    caretaker.undo()
    assert originator.get_state() == "State #2"
    assert caretaker.get_history_length() == 1

    # Undo 2: returns to State #1
    caretaker.undo()
    assert originator.get_state() == "State #1"
    assert caretaker.get_history_length() == 0

    # Undo 3: empty history has no effect, keeps State #1
    caretaker.undo()
    assert originator.get_state() == "State #1"
    assert caretaker.get_history_length() == 0
