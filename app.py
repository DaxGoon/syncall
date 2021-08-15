from flask import Flask
from gevent.pywsgi import WSGIServer
from flask_restful import Api
from resources import MessageSignConnector, DelayedResponseProvider

app = Flask(__name__)
api = Api(app)

api.add_resource(MessageSignConnector, "/crypto/sign")
api.add_resource(DelayedResponseProvider, "/delayed_response")


if __name__ == "__main__":
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
    app.run(port=5000, debug=True)
