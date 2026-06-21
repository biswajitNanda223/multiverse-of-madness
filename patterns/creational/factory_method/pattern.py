from abc import ABC, abstractmethod


class Transport(ABC):
    """The Product interface declares the operations all concrete products must implement."""

    @abstractmethod
    def deliver(self) -> str:
        """Performs the delivery action."""
        pass


class Truck(Transport):
    """Concrete Product implementation for road logistics."""

    def deliver(self) -> str:
        """Delivers cargo by land."""
        return "Delivering by land in a container truck."


class Ship(Transport):
    """Concrete Product implementation for sea logistics."""

    def deliver(self) -> str:
        """Delivers cargo by sea."""
        return "Delivering by sea in a cargo ship."


class Logistics(ABC):
    """The Creator class declares the factory method that returns a Product object."""

    @abstractmethod
    def create_transport(self) -> Transport:
        """The Factory Method.

        Subclasses override this method to return concrete Transport instances.
        """
        pass

    def plan_delivery(self) -> str:
        """Core business logic that relies on the Product returned by the factory method."""
        transport = self.create_transport()
        return f"Logistics: {transport.deliver()}"


class RoadLogistics(Logistics):
    """Concrete Creator overriding the factory method to return a Truck."""

    def create_transport(self) -> Transport:
        """Creates a Truck instance."""
        return Truck()


class SeaLogistics(Logistics):
    """Concrete Creator overriding the factory method to return a Ship."""

    def create_transport(self) -> Transport:
        """Creates a Ship instance."""
        return Ship()
