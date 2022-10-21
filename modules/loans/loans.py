from datetime import date as date_type
from fastapi import Request, status
from ...include import schemas
from ...include.exception_handler import ExceptionHandler
from decimal import *

class Loan():
    @classmethod
    def create_loan(cls, data: schemas.Loan, request: Request) -> schemas.Loan:
        # save the new loan. this will replace the previously created loan
        request.app.state.loanData['loan'] = {
            'amount': data.amount,
            'interest_rate': data.interest_rate,
            'start_date': data.start_date
        }
        # clear previously created payments
        request.app.state.loanData['payments'] = []
        return request.app.state.loanData['loan']


    @classmethod
    def get_loan(cls, request: Request) -> schemas.Loan:
        if not request.app.state.loanData['loan']:
            raise ExceptionHandler.raise_exception(status.HTTP_404_NOT_FOUND, 'No loan has been registered yet')
        else:
            return request.app.state.loanData['loan']


    @classmethod
    def get_balance(cls, target_date: date_type, request: Request) -> schemas.BalanceAmount:
        balanceAmount = 0
        if not request.app.state.loanData['loan']:
            raise ExceptionHandler.raise_exception(status.HTTP_404_NOT_FOUND, 'No loan has been registered yet')
        elif target_date >= request.app.state.loanData['loan']['start_date']:
            dailyInterestRate = request.app.state.loanData['loan']['interest_rate']/100/365
            baseAmount = request.app.state.loanData['loan']['amount']
            interestAmount = 0
            startDate = request.app.state.loanData['loan']['start_date']
            endDate = target_date

            for item in request.app.state.loanData['payments']:
                # item is a tuple:
                # item[0] is payment date
                # item[1] is a dict containing payment data = {date, amount}
                if startDate <= item[0] <= endDate:
                    #print(balanceAmount,balanceAmount*((item[0]-startDate).days * dailyInterestRate),item[1]['amount'])
                    interestAmount += baseAmount*((item[0]-startDate).days * dailyInterestRate)
                    baseAmount -= item[1]['amount']
                    if baseAmount<=0:
                        baseAmount = 0
                        break
                    startDate = item[0]
                    #print(balanceAmount,startDate)
            
            # this will be true if there are some remaining days between the last payment and the target date
            # basically, we are adding more interest to the balance
            if startDate < endDate:
                print(baseAmount,(baseAmount * ((endDate-startDate).days * dailyInterestRate)))
                interestAmount += (baseAmount * ((endDate-startDate).days * dailyInterestRate))
            
            balanceAmount = baseAmount + interestAmount
            # round up to TWO decimal points
            balanceAmount = balanceAmount.quantize(Decimal('.01'), rounding=ROUND_UP)
        
        return {'amount': balanceAmount}