import threading
from typing import Any, Dict


class SingletonMeta(type):
    """A thread-safe implementation of Singleton pattern using metaclasses."""

    _instances: Dict[type, Any] = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """Ensures only a single instance of the class is created across threads.

        Uses the double-checked locking pattern for optimal performance.
        """
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    """An example class representing a Singleton Database Connection."""

    def __init__(self, connection_string: str) -> None:
        """Initializes the database connection.

        Args:
            connection_string: The database URI/connection string.
        """
        self.connection_string = connection_string
        self.connected = False

    def connect(self) -> None:
        """Simulates establishing a database connection."""
        self.connected = True

    def disconnect(self) -> None:
        """Simulates closing a database connection."""
        self.connected = False
