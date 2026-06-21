import pytest

from patterns.structural.composite.pattern import Box, Product


def test_leaf_product() -> None:
    """Verifies that the product leaf holds values and raises errors on structural operations."""
    phone = Product("iPhone 15", 999.99)
    assert phone.get_name() == "iPhone 15"
    assert phone.get_price() == 999.99
    assert not phone.is_composite()

    charger = Product("Charger", 29.99)

    with pytest.raises(NotImplementedError):
        phone.add(charger)

    with pytest.raises(NotImplementedError):
        phone.remove(charger)


def test_nested_composite_price() -> None:
    """Verifies recursive price aggregation for nested boxes."""
    # Leaf items
    phone = Product("iPhone 15", 999.99)
    case = Product("Silicone Case", 49.00)
    charger = Product("Charger", 29.99)

    # Sub-box for accessories
    accessory_box = Box("Accessory Box")
    accessory_box.add(case)
    accessory_box.add(charger)
    assert accessory_box.is_composite()
    assert accessory_box.get_price() == 49.00 + 29.99

    # Main package box
    main_box = Box("Main Shipping Box")
    main_box.add(phone)
    main_box.add(accessory_box)

    expected_total = 999.99 + 49.00 + 29.99
    assert main_box.get_price() == expected_total

    # Test removing an element from a composite
    accessory_box.remove(charger)
    assert main_box.get_price() == 999.99 + 49.00
