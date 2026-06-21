from abc import ABC, abstractmethod
from typing import List

from .models import Split


class SplitStrategy(ABC):
    @abstractmethod
    def validate(self, splits: List[Split], total_amount: float) -> bool:
        """Validate if the splits conform to the splitting rules."""
        pass

    @abstractmethod
    def calculate_amounts(self, splits: List[Split], total_amount: float) -> None:
        """Calculate and set the amount for each split in-place."""
        pass


class EqualSplitStrategy(SplitStrategy):
    def validate(self, splits: List[Split], total_amount: float) -> bool:
        return len(splits) > 0

    def calculate_amounts(self, splits: List[Split], total_amount: float) -> None:
        if not self.validate(splits, total_amount):
            raise ValueError("Invalid splits for Equal split strategy.")

        num_splits = len(splits)
        split_amount = round(total_amount / num_splits, 2)

        # Adjust for rounding errors
        accumulated = 0.0
        for i, split in enumerate(splits):
            if i == num_splits - 1:
                split.amount = round(total_amount - accumulated, 2)
            else:
                split.amount = split_amount
                accumulated += split_amount


class ExactSplitStrategy(SplitStrategy):
    def validate(self, splits: List[Split], total_amount: float) -> bool:
        total_sum = sum(split.value for split in splits if split.value is not None)
        return abs(total_sum - total_amount) < 0.01

    def calculate_amounts(self, splits: List[Split], total_amount: float) -> None:
        if not self.validate(splits, total_amount):
            raise ValueError("Exact split sum does not match total expense amount.")

        for split in splits:
            split.amount = round(split.value or 0.0, 2)


class PercentSplitStrategy(SplitStrategy):
    def validate(self, splits: List[Split], total_amount: float) -> bool:
        total_percent = sum(split.value for split in splits if split.value is not None)
        return abs(total_percent - 100.0) < 0.01

    def calculate_amounts(self, splits: List[Split], total_amount: float) -> None:
        if not self.validate(splits, total_amount):
            raise ValueError("Percentage splits do not sum to 100%.")

        accumulated = 0.0
        num_splits = len(splits)
        for i, split in enumerate(splits):
            percent = split.value or 0.0
            if i == num_splits - 1:
                split.amount = round(total_amount - accumulated, 2)
            else:
                split.amount = round((percent * total_amount) / 100.0, 2)
                accumulated += split.amount
