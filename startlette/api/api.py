

from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse,Response, PlainTextResponse
from forms import QudraticModel
from pydantic import ValidationError
from calculate_x import calculate_x


# for running starlette
# checkout api folder and type this command 
# uvicorn api:app --reload


async def homepage(request:Request):
    return PlainTextResponse(content="Hello Shabeeb")


async def json_end_point(request:Request):
    return JSONResponse(content={"message":"Hello Shabeeb"})


async def quadratic_eqn(request:Request):
    if request.method == 'POST':
        data = await request.json()
        try:
            datas = QudraticModel(**data)
        except ValidationError as e:
            return JSONResponse({"error":e.json()})
        try:
            x1,x2 = calculate_x(datas.a,datas.b,datas.c)
            return JSONResponse({"x1":x1,"x2":x2})
        except ValueError:
            return JSONResponse({"error":"Invalid Input"})
    return JSONResponse(content={"message":"Hello Shabeeb"})


    

routes = [
    Route("/", endpoint=homepage),
    Route("/json",endpoint=json_end_point),
    Route('/api/',endpoint=quadratic_eqn,methods=["GET","POST"]),
]

app = Starlette(debug=True, routes=routes)
