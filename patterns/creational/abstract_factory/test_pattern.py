from patterns.creational.abstract_factory.pattern import (
    ModernChair,
    ModernFurnitureFactory,
    ModernSofa,
    VictorianChair,
    VictorianFurnitureFactory,
    VictorianSofa,
)


def test_victorian_factory() -> None:
    """Verifies Victorian factory creates Victorian-styled matching products."""
    factory = VictorianFurnitureFactory()
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    assert isinstance(chair, VictorianChair)
    assert isinstance(sofa, VictorianSofa)
    assert chair.sit_on() == "Sitting on a Victorian Chair with elegant carvings."
    assert sofa.lie_on() == "Lying on a Victorian Sofa made of red velvet."


def test_modern_factory() -> None:
    """Verifies Modern factory creates Modern-styled matching products."""
    factory = ModernFurnitureFactory()
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    assert isinstance(chair, ModernChair)
    assert isinstance(sofa, ModernSofa)
    assert chair.sit_on() == "Sitting on a sleek, minimalist Modern Chair."
    assert sofa.lie_on() == "Lying on a comfortable fabric Modern Sofa."
