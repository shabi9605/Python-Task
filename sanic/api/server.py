from sanic import Sanic
from sanic.response import text,json
from calculate_x import calculate_x
from forms import QudraticModel
from pydantic import ValidationError

# # for running sanic
# checkout api folder and type this command 
# sanic server

app = Sanic("MyHelloWorldApp")

@app.get("/")
async def hello_world(request):
    return text("Hello, world. shabeeb")


@app.post("/api/")
async def quadraic_eqn(request):
    data = request.json
    try:
        data = QudraticModel(**data)
    except ValidationError as e:
        return json({"error":e.json()})
    try:
        x1,x2 = calculate_x(data.a,data.b,data.c)
        return json({"x1":x1,"x2":x2})
    except ValueError:
        return json({"error":"Invalid Input"})



