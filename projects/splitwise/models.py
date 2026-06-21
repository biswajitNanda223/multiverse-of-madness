from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class SplitType(str, Enum):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"


class User(BaseModel):
    user_id: str
    name: str
    email: str


class Split(BaseModel):
    user_id: str
    amount: float = 0.0  # The calculated share of this user
    value: Optional[float] = (
        None  # Exact amount or percentage value depending on split type
    )


class Expense(BaseModel):
    expense_id: str
    description: str
    total_amount: float
    paid_by: str
    split_type: SplitType
    splits: List[Split]


class ExpenseGroup(BaseModel):
    group_id: str
    name: str
    members: List[str] = Field(default_factory=list)
    expenses: List[Expense] = Field(default_factory=list)
