
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from model import QudraticModel
from calculate_x import calculate_x

app = FastAPI()


# created custom exception handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error = {}
    validation_errors = exc.errors()
    for i in validation_errors:
        error[i["loc"][1]] = [i["msg"]]
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(error),
    )

@app.post("/api/")
async  def quadraic_eqn(q:QudraticModel):
    try:
        x1,x2 = calculate_x(q.a,q.b,q.c)
        return {"x1":x1,"x2":x2}
    except ValueError:
        return {"error":"Invalid Input"}
