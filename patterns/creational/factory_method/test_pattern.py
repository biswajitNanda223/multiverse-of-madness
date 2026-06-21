from patterns.creational.factory_method.pattern import (
    Logistics,
    RoadLogistics,
    SeaLogistics,
    Ship,
    Truck,
)


def test_road_logistics() -> None:
    """Verifies that RoadLogistics creates a Truck and delivers via land."""
    logistics: Logistics = RoadLogistics()
    transport = logistics.create_transport()

    assert isinstance(transport, Truck)
    assert transport.deliver() == "Delivering by land in a container truck."
    assert (
        logistics.plan_delivery()
        == "Logistics: Delivering by land in a container truck."
    )


def test_sea_logistics() -> None:
    """Verifies that SeaLogistics creates a Ship and delivers via sea."""
    logistics: Logistics = SeaLogistics()
    transport = logistics.create_transport()

    assert isinstance(transport, Ship)
    assert transport.deliver() == "Delivering by sea in a cargo ship."
    assert logistics.plan_delivery() == "Logistics: Delivering by sea in a cargo ship."
