from typing import Optional


class House:
    """The Product class representing the complex object under construction."""

    def __init__(self) -> None:
        self.walls: Optional[str] = None
        self.doors: int = 0
        self.windows: int = 0
        self.roof: Optional[str] = None
        self.garage: bool = False
        self.swimming_pool: bool = False
        self.garden: bool = False

    def __str__(self) -> str:
        return (
            f"Walls: {self.walls}, Doors: {self.doors}, Windows: {self.windows}, "
            f"Roof: {self.roof}, Garage: {self.garage}, Pool: {self.swimming_pool}, "
            f"Garden: {self.garden}"
        )


class HouseBuilder:
    """The Builder class providing step-by-step configuration for building a House."""

    def __init__(self) -> None:
        self._house: House = House()

    def reset(self) -> "HouseBuilder":
        """Resets the builder to construct a new House."""
        self._house = House()
        return self

    def build_walls(self, wall_type: str) -> "HouseBuilder":
        """Sets the type of walls."""
        self._house.walls = wall_type
        return self

    def build_doors(self, count: int) -> "HouseBuilder":
        """Sets the number of doors."""
        self._house.doors = count
        return self

    def build_windows(self, count: int) -> "HouseBuilder":
        """Sets the number of windows."""
        self._house.windows = count
        return self

    def build_roof(self, roof_type: str) -> "HouseBuilder":
        """Sets the roof type."""
        self._house.roof = roof_type
        return self

    def build_garage(self) -> "HouseBuilder":
        """Adds a garage to the house configuration."""
        self._house.garage = True
        return self

    def build_swimming_pool(self) -> "HouseBuilder":
        """Adds a swimming pool."""
        self._house.swimming_pool = True
        return self

    def build_garden(self) -> "HouseBuilder":
        """Adds a garden."""
        self._house.garden = True
        return self

    def get_result(self) -> House:
        """Retrieves the fully constructed House and resets the builder."""
        product = self._house
        self.reset()
        return product


class Director:
    """The Director defines the order of building steps to create predefined house models."""

    def __init__(self, builder: HouseBuilder) -> None:
        """Initializes the Director with a specific builder.

        Args:
            builder: The HouseBuilder instance to use.
        """
        self._builder = builder

    def build_minimal_house(self) -> House:
        """Constructs a basic house model."""
        return (
            self._builder.reset()
            .build_walls("Brick")
            .build_doors(1)
            .build_windows(2)
            .build_roof("Shingle")
            .get_result()
        )

    def build_luxury_house(self) -> House:
        """Constructs a full luxury house model."""
        return (
            self._builder.reset()
            .build_walls("Marble")
            .build_doors(5)
            .build_windows(10)
            .build_roof("Slate")
            .build_garage()
            .build_swimming_pool()
            .build_garden()
            .get_result()
        )
