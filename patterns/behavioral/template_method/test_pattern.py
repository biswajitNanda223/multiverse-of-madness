from patterns.behavioral.template_method.pattern import BrickHouse, WoodenHouse


def test_wooden_house_template() -> None:
    """Verifies that the WoodenHouse follows the construction steps without the hook."""
    builder = WoodenHouse()
    steps = builder.build_house()

    assert len(steps) == 4
    assert steps[0] == "Foundation: Laying concrete foundation."
    assert steps[1] == "Walls: Erecting wooden log walls."
    assert steps[2] == "Roof: Installing wood shingle roof."
    assert steps[3] == "Windows: Installing glass windows."


def test_brick_house_template() -> None:
    """Verifies that the BrickHouse follows construction steps and executes the hook."""
    builder = BrickHouse()
    steps = builder.build_house()

    assert len(steps) == 5
    assert steps[0] == "Foundation: Laying concrete foundation."
    assert steps[1] == "Walls: Laying brick walls with mortar."
    assert steps[2] == "Roof: Installing slate roof."
    assert steps[3] == "Windows: Installing glass windows."
    assert steps[4] == "Decorations: Painting walls and hanging a flag."
