from pydantic import BaseModel
from pydantic import root_validator

class QudraticModel(BaseModel):
    a: float
    b: float
    c: float

    @root_validator
    def check_a(cls, values):
        if values.get("a") == 0:
            raise ValueError("The value of a not equal to zero")
        return values