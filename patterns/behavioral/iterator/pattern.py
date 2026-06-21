from collections.abc import Iterable, Iterator
from typing import List, Optional


class AlphabeticalOrderIterator(Iterator):
    """Concrete Iterator implementing alphabetical collection traversal.

    Tracks current state and index position.
    """

    def __init__(self, collection: "WordsCollection", reverse: bool = False) -> None:
        """Initializes the Iterator.

        Args:
            collection: The WordsCollection instance.
            reverse: True for reverse order traversal, False for normal.
        """
        self._collection = collection
        self._reverse = reverse
        self._position = len(collection) - 1 if reverse else 0

    def __next__(self) -> str:
        """Returns the next element in the collection or raises StopIteration."""
        if self._reverse and self._position < 0:
            raise StopIteration()
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
            return value
        except IndexError:
            raise StopIteration()


class WordsCollection(Iterable):
    """Concrete Collection offering forward and reverse custom iterators."""

    def __init__(self, items: Optional[List[str]] = None) -> None:
        self._items = items or []

    def __iter__(self) -> AlphabeticalOrderIterator:
        """Default iterator (forward direction)."""
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        """Custom iterator in reverse direction."""
        return AlphabeticalOrderIterator(self, reverse=True)

    def add_item(self, item: str) -> None:
        """Adds a new item to the collection."""
        self._items.append(item)

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int) -> str:
        return self._items[index]
