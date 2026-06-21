from typing import List

from patterns.behavioral.visitor.pattern import (
    Circle,
    Dot,
    JSONExportVisitor,
    ShapeElement,
    XMLExportVisitor,
)


def test_xml_export_visitor() -> None:
    """Verifies XML visitor output on Dot and Circle elements."""
    dot = Dot(1, 2)
    circle = Circle(5)
    xml_visitor = XMLExportVisitor()

    assert dot.accept(xml_visitor) == '<dot x="1" y="2"/>'
    assert circle.accept(xml_visitor) == '<circle radius="5"/>'


def test_json_export_visitor() -> None:
    """Verifies JSON visitor output on Dot and Circle elements."""
    dot = Dot(10, 20)
    circle = Circle(15)
    json_visitor = JSONExportVisitor()

    assert dot.accept(json_visitor) == '{"type": "dot", "x": 10, "y": 20}'
    assert circle.accept(json_visitor) == '{"type": "circle", "radius": 15}'


def test_batch_visiting() -> None:
    """Verifies visiting a list of elements using both visitors."""
    shapes: List[ShapeElement] = [Dot(0, 0), Circle(10)]
    xml_visitor = XMLExportVisitor()
    json_visitor = JSONExportVisitor()

    xml_results = [shape.accept(xml_visitor) for shape in shapes]
    json_results = [shape.accept(json_visitor) for shape in shapes]

    assert xml_results == ['<dot x="0" y="0"/>', '<circle radius="10"/>']
    assert json_results == [
        '{"type": "dot", "x": 0, "y": 0}',
        '{"type": "circle", "radius": 10}',
    ]
