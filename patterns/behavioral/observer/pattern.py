from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """The Observer interface defines the update notification method."""

    @abstractmethod
    def update(self, subject: "Subject") -> str:
        """Receives update signals from the subject."""
        pass


class Subject(ABC):
    """The Subject interface declaring methods to attach/detach observers."""

    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        """Subscribes an observer."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Unsubscribes an observer."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self) -> List[str]:
        """Notifies all registered observers of state changes."""
        return [observer.update(self) for observer in self._observers]


class NewsPublisher(Subject):
    """Concrete Subject that broadcasts published news articles."""

    def __init__(self) -> None:
        super().__init__()
        self._latest_news: str = ""

    @property
    def latest_news(self) -> str:
        """Gets the latest published news string."""
        return self._latest_news

    def publish_news(self, news: str) -> List[str]:
        """Sets news state and fires notification broadcast."""
        self._latest_news = news
        return self.notify()


class NewsSubscriber(Observer):
    """Concrete Observer representing a news subscriber client."""

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, subject: Subject) -> str:
        if isinstance(subject, NewsPublisher):
            return f"Subscriber {self.name} notified: '{subject.latest_news}'"
        return f"Subscriber {self.name} notified."
