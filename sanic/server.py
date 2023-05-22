from sanic import Sanic
from sanic.response import text

app = Sanic("MyHelloWorldApp")

@app.get("/")
async def hello_world(request):
    return text("Hello, world. shabeeb")


@app.post("/api/")
async def quadraic_eqn(request):
    print("request ===> ",request.json)
    return text("Hello, world. shabeeb")



