from fastapi import HTTPException


class ExceptionHandler():
        @classmethod
        def raise_exception(cls, code: int, detail: str):
                # log the exception
                # -- NOT IMPLEMENTED --

                # raise the exception
                raise HTTPException(status_code = code, detail = detail)