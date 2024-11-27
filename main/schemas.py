from ninja import Schema
from datetime import date
from datetime import datetime
from pydantic import BaseModel
from decimal import Decimal


class SignUpSchema(Schema):
    username: str
    password: str
    email: str | None = None


class LoginSchema(Schema):
    username: str
    password: str


class TokenResponse(Schema):
    access: str
    refresh: str
    user: dict


class AWBCreateSchema(Schema):
    awb_number: str


class AWBSchema(BaseModel):
    id: int
    awb_number: str
    created_at: datetime

    class Config:
        arbitrary_types_allowed = True
        from_attributes=True


class AWBSummarySchema(Schema):
    total: int
    delivered: int
    pending: int

    class Config:
        arbitrary_types_allowed = True
        from_attributes=True


class CostSummarySchema(Schema):
    totalCosts: float
    completed: int
    pending: int

    class Config:
        arbitrary_types_allowed = True
        from_attributes=True


class AWBDetailsSchema(Schema):
    id: int
    awb_number: str
    created_at: str
    total_cost: float
    profit: float

    class Config:
        arbitrary_types_allowed = True
        from_attributes=True


class CostUpdateSchema(Schema):
    amount: Decimal
    remarks: str | None = None

    class Config:
        arbitrary_types_allowed = True
        from_attributes=True


class CostSchema(BaseModel):
    id: int
    name: str
    amount: float
    remarks: str

    class Config:
        arbitrary_types_allowed = True
        from_attributes=True


class CostCreateSchema(Schema):
    awb_id: int
    name: str
    amount: Decimal
    remarks: str | None = None

    class Config:
        arbitrary_types_allowed = True
        from_attributes=True


class ProfitLossSchema(Schema):
    revenue: float
    total_cost: float
    profit: float
    loss: float

    class Config:
        arbitrary_types_allowed = True
        from_attributes=True
