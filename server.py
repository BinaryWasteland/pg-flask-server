from flask import Flask
from flask import jsonify
from flask_cors import CORS
import docker
import logging, sys

app = Flask(__name__)
CORS(app)

client = docker.from_env()

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.debug('A debug message!')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/restart-numbra')
def restart_numbra():
    container = client.containers.get('sloppydrive-pgnumbra')
    logging.debug(container)
    container.restart()
    return make_api_success_response(200, 'success')


def make_api_success_response(status, data):
    return jsonify({'status': status, 'data': data})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)
