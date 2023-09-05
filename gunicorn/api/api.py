import json
from io import BytesIO

# for running gunicorn
# checkout api folder and type this command 
# We cannot run gunicorn on windows, we need wsl or ubuntu
# gunicorn --workers=2 api:app --reload

from calculate_x import calculate_x

def app(environ, start_response):
    status = '200 OK'
    
    length = int(environ.get('CONTENT_LENGTH') or 0)
    body = environ['wsgi.input'].read(length)
    environ['body_copy'] = body
    body = json.loads(environ['body_copy'])

    try:
        if body["a"] == 0:
            data = json.dumps({"error":"The value of a not equal to zero"}).encode('utf-8')
            response_headers = [
                ('Content-type', 'json'),
                ('Content-Length', str(len(data)))
            ]
            start_response(status, response_headers)
            
            return iter([data])
        
        data = calculate_x(body["a"],body["b"],body["c"])
        data = str(data)
        data = json.dumps(data, indent=2).encode('utf-8')
        
    except ValueError:
        data = json.dumps({"error":"Invalid Input"}).encode('utf-8')
    
    response_headers = [
        ('Content-type', 'json'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    
    return iter([data])


