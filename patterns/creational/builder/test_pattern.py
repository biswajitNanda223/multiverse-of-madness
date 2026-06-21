from patterns.creational.builder.pattern import Director, HouseBuilder


def test_custom_house_builder() -> None:
    """Verifies that a client can build a custom house step-by-step."""
    builder = HouseBuilder()
    house = (
        builder.build_walls("Wood")
        .build_doors(2)
        .build_windows(4)
        .build_roof("Wood Shingles")
        .build_garden()
        .get_result()
    )

    assert house.walls == "Wood"
    assert house.doors == 2
    assert house.windows == 4
    assert house.roof == "Wood Shingles"
    assert not house.garage
    assert not house.swimming_pool
    assert house.garden


def test_director_minimal_house() -> None:
    """Verifies director can construct a minimal house correctly."""
    builder = HouseBuilder()
    director = Director(builder)
    house = director.build_minimal_house()

    assert house.walls == "Brick"
    assert house.doors == 1
    assert house.windows == 2
    assert house.roof == "Shingle"
    assert not house.garage
    assert not house.swimming_pool
    assert not house.garden


def test_director_luxury_house() -> None:
    """Verifies director can construct a luxury house correctly."""
    builder = HouseBuilder()
    director = Director(builder)
    house = director.build_luxury_house()

    assert house.walls == "Marble"
    assert house.doors == 5
    assert house.windows == 10
    assert house.roof == "Slate"
    assert house.garage
    assert house.swimming_pool
    assert house.garden
