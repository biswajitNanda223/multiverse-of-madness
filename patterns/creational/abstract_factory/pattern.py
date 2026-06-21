from abc import ABC, abstractmethod


# Abstract Products
class Chair(ABC):
    """Abstract Product A: Chair."""

    @abstractmethod
    def sit_on(self) -> str:
        """Actions on a chair."""
        pass


class Sofa(ABC):
    """Abstract Product B: Sofa."""

    @abstractmethod
    def lie_on(self) -> str:
        """Actions on a sofa."""
        pass


# Concrete Products: Victorian Style
class VictorianChair(Chair):
    """Concrete Product A1: Victorian-style Chair."""

    def sit_on(self) -> str:
        """Sits on Victorian chair."""
        return "Sitting on a Victorian Chair with elegant carvings."


class VictorianSofa(Sofa):
    """Concrete Product B1: Victorian-style Sofa."""

    def lie_on(self) -> str:
        """Lies on Victorian sofa."""
        return "Lying on a Victorian Sofa made of red velvet."


# Concrete Products: Modern Style
class ModernChair(Chair):
    """Concrete Product A2: Modern-style Chair."""

    def sit_on(self) -> str:
        """Sits on Modern chair."""
        return "Sitting on a sleek, minimalist Modern Chair."


class ModernSofa(Sofa):
    """Concrete Product B2: Modern-style Sofa."""

    def lie_on(self) -> str:
        """Lies on Modern sofa."""
        return "Lying on a comfortable fabric Modern Sofa."


# Abstract Factory
class FurnitureFactory(ABC):
    """Abstract Factory interface for creating families of matching furniture."""

    @abstractmethod
    def create_chair(self) -> Chair:
        """Creates an abstract Chair product."""
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        """Creates an abstract Sofa product."""
        pass


# Concrete Factories
class VictorianFurnitureFactory(FurnitureFactory):
    """Concrete Factory producing Victorian-style furniture."""

    def create_chair(self) -> Chair:
        """Produces a Victorian Chair."""
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        """Produces a Victorian Sofa."""
        return VictorianSofa()


class ModernFurnitureFactory(FurnitureFactory):
    """Concrete Factory producing Modern-style furniture."""

    def create_chair(self) -> Chair:
        """Produces a Modern Chair."""
        return ModernChair()

    def create_sofa(self) -> Sofa:
        """Produces a Modern Sofa."""
        return ModernSofa()
