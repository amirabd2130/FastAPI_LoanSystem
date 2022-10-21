from typing import List
from fastapi import APIRouter, status, Request
from ..include import schemas
from ..modules.payments.payments import Payment


router = APIRouter(
    prefix = '/payment',
    tags = ['Payment'],
)


@router.post('/', status_code = status.HTTP_201_CREATED)
def create_payment(data: schemas.Payment, request: Request):
    return Payment.create_payment(data, request)


@router.get('/', status_code = status.HTTP_200_OK, response_model = List[schemas.Payment])
def get_all_payments(request: Request):
    return Payment.get_all_payments(request)