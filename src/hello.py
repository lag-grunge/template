import json
from flask import Flask, request
from werkzeug.exceptions import BadRequest
from db import insert_db, read_db, update_db

app = Flask(__name__)


@app.post('/get_form/')
def get():
    resp = read_db(document=request.args)
    return resp
    

@app.post('/create_form/')
def create():
    if not 'name' in request.args:
        raise BadRequest(request.args)
    resp = insert_db(document=request.args)
    return resp


@app.put('/update_form/')
def update():
    if not 'name' in request.args:
        raise BadRequest(request.args)
    resp = update_db(document=request.args)
    return resp


@app.errorhandler(400)
def bad_request_error_handler(e):
     return json.dumps({"error": "BadRequest", "args": list(request.args)}), BadRequest.code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
