from typing import List
from fastapi import Request, status
import bisect
from ...include import schemas
from ...include.exception_handler import ExceptionHandler


class Payment():
    @classmethod
    def create_payment(cls, data: schemas.Payment, request: Request) -> schemas.Payment:
        if not request.app.state.loanData['loan']:
            raise ExceptionHandler.raise_exception(status.HTTP_404_NOT_FOUND, 'No loan has been registered yet')
        elif data.date < request.app.state.loanData['loan']['start_date']:
            raise ExceptionHandler.raise_exception(status.HTTP_400_BAD_REQUEST, 'Provided date is before starting date of current loan')
        else:
            # create and maintain a sorted list of payments, sorted by payment's date
            bisect.insort_left(request.app.state.loanData['payments'], (data.date, dict(data)), key=lambda x: x[0])
            return data


    @classmethod
    def get_all_payments(cls, request: Request) -> List[schemas.Payment]:
        return [item[1] for item in request.app.state.loanData['payments']]