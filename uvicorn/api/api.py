
# for running uvicorn
# checkout api folder and type this command 
# uvicorn api:app --reload
from calculate_x import calculate_x
import ast
import json



async def app(scope, receive, send):
    assert scope['type'] == 'http'

    message = await receive()
    body = message["body"]
    body = body.decode("UTF-8")
    body = ast.literal_eval(body)
    try:
        data = calculate_x(body["a"],body["b"],body["c"])
        
    except KeyError:
        if ("a" in body) == False:
            data = {"error":"Please enter the value of a "}
        elif ("b" in body) == False:
            data = {"error":"Please enter the value of b "}
        else:
            data = {"error":"Please enter the value of c "}

    data = json.dumps(data).encode('utf-8')

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            (b'content-type', b'text/plain'),
            (b'content-length', str(len(data)).encode())
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': data,
    })