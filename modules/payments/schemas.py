from datetime import date as date_type
from decimal import Decimal
from pydantic import BaseModel


class Payment(BaseModel):
    amount: Decimal
    date: date_type