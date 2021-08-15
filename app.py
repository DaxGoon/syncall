from flask import Flask
from gevent.pywsgi import WSGIServer
from flask_restful import Api
from resources import MessageSignConnector

app = Flask(__name__)
api = Api(app)

api.add_resource(
    MessageSignConnector, "/crypto/sign/<string:message>"
)

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
