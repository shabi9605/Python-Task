from json import dumps, loads
from flask import Flask, jsonify, request
import json
from forms import QuadraticForm
from calculate_x import calculate_x
from marshmallow import ValidationError
import jsonpickle

# to run flask you can use 'flask run' command or 'python -m flask run'


app = Flask(__name__)

@app.route("/api/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        body = json.loads(request.data.decode("utf-8")) # this converting to python objects because its getting as a string
        form = QuadraticForm()
        try:
            result = form.load(body)
        except ValidationError as err:
            return err.messages

        try:
            x1,x2 = calculate_x(body["a"],body["b"],body["c"])
            return {"x1":x1,"x2":x2}
        except ValueError:
            return {"error":"Invalid Input"}
        



if __name__=='__main__':
    app.run(debug=True)





