from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    """The Strategy interface declares operations common to all supported
    versions of some algorithm.
    """

    @abstractmethod
    def build_route(self, start: str, end: str) -> str:
        """Generates navigation directions between start and end locations."""
        pass


class RoadStrategy(RouteStrategy):
    """Concrete Strategy: Road Route."""

    def build_route(self, start: str, end: str) -> str:
        return f"Road route from {start} to {end} via highways."


class PublicTransportStrategy(RouteStrategy):
    """Concrete Strategy: Public Transport Route."""

    def build_route(self, start: str, end: str) -> str:
        return f"Public transport route from {start} to {end} via bus/subway."


class WalkingStrategy(RouteStrategy):
    """Concrete Strategy: Walking Route."""

    def build_route(self, start: str, end: str) -> str:
        return f"Walking path route from {start} to {end} via sidewalks."


class Navigator:
    """The Context class that delegates route calculation to a RouteStrategy."""

    def __init__(self, strategy: RouteStrategy) -> None:
        """Initializes Navigator with a strategy.

        Args:
            strategy: The initial routing algorithm strategy.
        """
        self._strategy = strategy

    @property
    def strategy(self) -> RouteStrategy:
        """Gets current routing strategy."""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: RouteStrategy) -> None:
        """Sets new routing strategy at runtime."""
        self._strategy = strategy

    def calculate_route(self, start: str, end: str) -> str:
        """Delegates calculations to the selected strategy."""
        return self._strategy.build_route(start, end)
