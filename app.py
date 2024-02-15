from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def home():
    html = f"<h1>Flask here, hoping to run in a container on aws apprunner and gcp cloudrun</h1>"
    return html.format(format)

@app.route('/hello/<name>')
def hello(name):
    message= f"Hello: {name}"
    return jsonify(message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
