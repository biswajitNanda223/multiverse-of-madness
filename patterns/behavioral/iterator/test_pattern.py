from patterns.behavioral.iterator.pattern import WordsCollection


def test_forward_iterator() -> None:
    """Verifies forward iteration traversal."""
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    results = []
    for item in collection:
        results.append(item)

    assert results == ["First", "Second", "Third"]


def test_reverse_iterator() -> None:
    """Verifies custom reverse iterator traversal."""
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    iterator = collection.get_reverse_iterator()

    results = []
    while True:
        try:
            results.append(next(iterator))
        except StopIteration:
            break

    assert results == ["Third", "Second", "First"]
