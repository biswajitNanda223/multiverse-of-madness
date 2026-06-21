from patterns.behavioral.strategy.pattern import (
    Navigator,
    PublicTransportStrategy,
    RoadStrategy,
    WalkingStrategy,
)


def test_routing_strategies() -> None:
    """Verifies that Navigator calculates directions correctly using different strategies."""
    road = RoadStrategy()
    transit = PublicTransportStrategy()
    walk = WalkingStrategy()

    # Initialize with road
    navigator = Navigator(road)
    assert (
        navigator.calculate_route("Home", "Work")
        == "Road route from Home to Work via highways."
    )

    # Change to transit
    navigator.strategy = transit
    assert (
        navigator.calculate_route("Home", "Work")
        == "Public transport route from Home to Work via bus/subway."
    )

    # Change to walking
    navigator.strategy = walk
    assert (
        navigator.calculate_route("Home", "Work")
        == "Walking path route from Home to Work via sidewalks."
    )
