import threading
from typing import List

from patterns.creational.singleton.pattern import DatabaseConnection


def test_singleton_identity() -> None:
    """Verifies that multiple instantiations of the Singleton return the same object."""
    db1 = DatabaseConnection("postgresql://localhost:5432/db")
    db2 = DatabaseConnection(
        "mysql://localhost:3306/db"
    )  # init might run or be ignored depending on python call protocol

    assert db1 is db2
    assert db1.connection_string == db2.connection_string


def test_singleton_state_sharing() -> None:
    """Verifies that modifications to one reference affect all references."""
    db1 = DatabaseConnection("postgresql://localhost:5432/db")
    db2 = DatabaseConnection("postgresql://localhost:5432/db")

    assert not db1.connected
    db1.connect()
    assert db2.connected

    db2.disconnect()
    assert not db1.connected


def test_singleton_thread_safety() -> None:
    """Verifies that multiple threads obtain the same instance of the Singleton."""
    instances: List[DatabaseConnection] = []

    def get_instance() -> None:
        db = DatabaseConnection("postgresql://localhost:5432/db")
        instances.append(db)

    threads = [threading.Thread(target=get_instance) for _ in range(50)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    first_instance = instances[0]
    for instance in instances:
        assert instance is first_instance
