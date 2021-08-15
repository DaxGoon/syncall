from flask import Flask
from gevent.pywsgi import WSGIServer
from flask_restful import Api

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
