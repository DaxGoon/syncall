import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from gevent.pywsgi import WSGIServer
from flask_restful import Api
from resources import MessageSignConnector, DelayedResponseProvider

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "db.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

api = Api(app)
api.add_resource(MessageSignConnector, "/crypto/sign")
api.add_resource(DelayedResponseProvider, "/delayed_response")

if __name__ == "__main__":
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
    app.run(port=5000, debug=True)
