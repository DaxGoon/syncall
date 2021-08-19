import os
from typing import Any

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_socketio import SocketIO  # &#
from flask_sqlalchemy import SQLAlchemy

from resources import MessageSignConnector, DelayedResponseProvider

app: Flask = Flask(__name__)
socketio: SocketIO = SocketIO(app)

basedir: Any = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "db.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db: SQLAlchemy = SQLAlchemy(app)
ma = Marshmallow(app)

api = Api(app)
api.add_resource(MessageSignConnector, "/crypto/sign")
api.add_resource(DelayedResponseProvider, "/delayed_response")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, use_reloader=False, debug=False)
