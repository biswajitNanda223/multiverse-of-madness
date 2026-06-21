from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .models import SplitType
from .service import SplitwiseService

app = FastAPI(
    title="Splitwise LLD API",
    description="Low-Level Design implementation of Splitwise with Equal, Exact, and Percentage Split strategies and Debt Simplification algorithm.",
    version="1.0.0",
)

# Instantiate Service
splitwise_service = SplitwiseService()


# Request/Response Schemas
class CreateUserRequest(BaseModel):
    user_id: str = Field(..., description="Unique alphanumeric identifier for the user")
    name: str = Field(..., description="Display name of the user")
    email: str = Field(..., description="User's email address")


class CreateGroupRequest(BaseModel):
    group_id: str = Field(..., description="Unique group identifier")
    name: str = Field(..., description="Name of the group")


class AddMemberRequest(BaseModel):
    user_id: str = Field(..., description="ID of the user to add")


class SplitInput(BaseModel):
    user_id: str = Field(..., description="Participant user ID")
    value: Optional[float] = Field(
        None, description="Exact amount or percentage (not needed for EQUAL split)"
    )


class AddExpenseRequest(BaseModel):
    description: str = Field(..., description="Brief description of the expense")
    total_amount: float = Field(..., gt=0, description="Total cost of the expense")
    paid_by: str = Field(..., description="User ID of the payer")
    split_type: SplitType = Field(
        ..., description="Type of split: EQUAL, EXACT, or PERCENT"
    )
    splits: List[SplitInput] = Field(..., description="List of participant splits")


# Endpoints
@app.post("/users", tags=["Users"])
def create_user(request: CreateUserRequest):
    try:
        user = splitwise_service.add_user(request.user_id, request.name, request.email)
        return {"status": "success", "user": user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/groups", tags=["Groups"])
def create_group(request: CreateGroupRequest):
    try:
        group = splitwise_service.create_group(request.group_id, request.name)
        return {"status": "success", "group": group}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/groups/{group_id}/members", tags=["Groups"])
def add_group_member(group_id: str, request: AddMemberRequest):
    try:
        splitwise_service.add_user_to_group(group_id, request.user_id)
        return {
            "status": "success",
            "message": f"User {request.user_id} added to group {group_id}.",
        }
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.post("/groups/{group_id}/expenses", tags=["Expenses"])
def add_expense(group_id: str, request: AddExpenseRequest):
    try:
        # Convert SplitInput to service models.Split
        from .models import Split

        splits = [Split(user_id=s.user_id, value=s.value) for s in request.splits]

        expense = splitwise_service.add_expense(
            group_id=group_id,
            description=request.description,
            total_amount=request.total_amount,
            paid_by=request.paid_by,
            split_type=request.split_type,
            splits=splits,
        )
        return {"status": "success", "expense": expense}
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/groups/{group_id}/balances", tags=["Balances & Settlements"])
def get_group_balances(group_id: str):
    try:
        return splitwise_service.get_balances(group_id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/groups/{group_id}/simplify", tags=["Balances & Settlements"])
def simplify_group_debts(group_id: str):
    try:
        transactions = splitwise_service.simplify_debts(group_id)
        return {"settlements": transactions}
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
