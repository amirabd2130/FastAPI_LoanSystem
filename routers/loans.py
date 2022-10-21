from datetime import date as date_type
from fastapi import APIRouter, status, Request
from ..include import schemas
from ..modules.loans.loans import Loan


router = APIRouter(
    prefix = '/loan',
    tags = ['Loan'],
)


@router.post('/', status_code = status.HTTP_201_CREATED)
def create_loan(data: schemas.Loan, request: Request):
    return Loan.create_loan(data, request)


@router.get('/', status_code = status.HTTP_200_OK, response_model = schemas.Loan)
def get_loan(request: Request):
    return Loan.get_loan(request)


@router.get('/balance/{target_date}', status_code = status.HTTP_200_OK, response_model = schemas.BalanceAmount)
def get_balance(target_date: date_type, request: Request):
    return Loan.get_balance(target_date, request)