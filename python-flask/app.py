import json

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

from main import main

app = Flask(__name__)


@app.errorhandler(HTTPException)
def handle_http_exception(e: HTTPException):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.status_code = e.code
    response.content_type = "application/json"
    return response


@app.errorhandler(Exception)
def handle_general_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    response = jsonify({
        "code": 500,
        "name": "Internal Server Error",
        "description": "Something went wrong.",
    })
    response.status_code = 500
    return response


@app.route('/webhook', methods=['POST'])
def hello_world():
    params = request.get_json(silent=True)

    if params is None:
        params = {}

    response = main(params)
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
