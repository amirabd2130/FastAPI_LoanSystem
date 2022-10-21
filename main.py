from fastapi import FastAPI
from .routers import loans, payments


description = '''
A simple Loan System API, created by using FastAPI

You can create a loan, add payment(s) to that loan and check balance amount for a certain data

Entities:
* **Loans**
* **Payments**
'''

app = FastAPI(
    title = 'Loan System API',
    description = description,
    version = '0.1',
    contact = {
        'name': 'Amir Abdollahi',
    },
    openapi_tags = [
        {
            'name': 'Loan',
            'description': 'Operations with loan, including creating  a load, retrieving a load, and getting balance amount',
        },
        {
            'name': 'Payment',
            'description': 'Operations with payments, including creating a payment and retrieving payments list',
        },
    ]
)


app.state.loanData = {
    'loan': {},
    'payments': []
}
app.include_router(loans.router)
app.include_router(payments.router)
