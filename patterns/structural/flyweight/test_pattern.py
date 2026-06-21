from patterns.structural.flyweight.pattern import Forest, TreeFactory


def test_flyweight_sharing() -> None:
    """Verifies that multiple trees of the same type share a single TreeType instance."""
    TreeFactory.clear()
    forest = Forest()

    # Plant 3 identical tree types at different coordinates
    t1 = forest.plant_tree(10, 20, "Oak", "Green", "Rough")
    t2 = forest.plant_tree(50, 100, "Oak", "Green", "Rough")
    t3 = forest.plant_tree(20, 40, "Oak", "Green", "Rough")

    assert t1.type is t2.type
    assert t2.type is t3.type
    assert TreeFactory.get_count() == 1


def test_flyweight_multiple_types() -> None:
    """Verifies that different tree configurations create new TreeType instances."""
    TreeFactory.clear()
    forest = Forest()

    t1 = forest.plant_tree(10, 20, "Oak", "Green", "Rough")
    t2 = forest.plant_tree(50, 100, "Birch", "White", "Smooth")
    t3 = forest.plant_tree(20, 40, "Oak", "Red", "Rough")  # variant color

    assert t1.type is not t2.type
    assert t1.type is not t3.type
    assert TreeFactory.get_count() == 3


def test_forest_draw() -> None:
    """Verifies rendering output for the entire forest."""
    TreeFactory.clear()
    forest = Forest()
    forest.plant_tree(1, 2, "Oak", "Green", "Rough")
    forest.plant_tree(10, 20, "Birch", "White", "Smooth")

    draw_output = forest.draw()
    assert len(draw_output) == 2
    assert draw_output[0] == "Tree Oak (Green/Rough) at (1, 2)"
    assert draw_output[1] == "Tree Birch (White/Smooth) at (10, 20)"
