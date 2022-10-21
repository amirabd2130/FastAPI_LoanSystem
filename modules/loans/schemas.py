from datetime import date as date_type
from decimal import Decimal
from pydantic import BaseModel


class Loan(BaseModel):
    amount: Decimal
    interest_rate: Decimal
    start_date: date_type


class BalanceDate(BaseModel):
    target_date: date_type


class BalanceAmount(BaseModel):
    amount: Decimal