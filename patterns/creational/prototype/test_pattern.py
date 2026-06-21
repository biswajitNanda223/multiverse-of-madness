from patterns.creational.prototype.pattern import ConcretePrototype


def test_prototype_clone_identity() -> None:
    """Verifies that cloned object is a different instance with same values."""
    p1 = ConcretePrototype("Original", ["v1", "v2"])
    p2 = p1.clone()

    assert p1 is not p2
    assert p1.name == p2.name
    assert p1.tags == p2.tags


def test_prototype_deep_copy() -> None:
    """Verifies that modifications to mutable structures on the clone do not affect the original."""
    p1 = ConcretePrototype("Original", ["v1", "v2"])
    p2 = p1.clone()

    p2.add_tag("v3")
    p2.name = "Cloned"

    assert "v3" in p2.tags
    assert "v3" not in p1.tags
    assert p1.name == "Original"


def test_prototype_circular_reference() -> None:
    """Verifies that circular references are preserved and cloned properly."""
    p1 = ConcretePrototype("Original", ["v1"])
    p1.circular_ref = p1  # Self reference

    p2 = p1.clone()

    assert p2 is not p1
    assert p2.circular_ref is p2  # Clone points to itself, not to the original
    assert p2.circular_ref is not p1.circular_ref
