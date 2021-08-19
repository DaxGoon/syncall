import threading

import requests
from flask import jsonify, Response
from flask_restful import request, Resource

from config import Config
from utils import keep_calling_on_failure

SYNTHESIA_ENDPOINT: str = Config.synthesia_api_endpoint
Q_P_KEY: str = Config.synthesia_api_sign_query_param_key
API_KEY: str = Config.synthesia_api_key


class MessageSignConnector(Resource):
    """
    Represent original API's Sign service by accepting and forwarding calls to it and returning either a valid response
     if available or a custom response with useful information to the client.
    """

    def get(self) -> Response:

        args = request.args
        message = str(args["message"])
        headers = {"Content-Type": "application/json", "Authorization": API_KEY}
        try:
            res = requests.get(
                SYNTHESIA_ENDPOINT + Q_P_KEY + message, headers=headers, timeout=2
            )

            if res.ok:
                return jsonify(res.text)
            else:
                thread = threading.Thread(
                    target=keep_calling_on_failure,
                    kwargs={
                        "full_uri": SYNTHESIA_ENDPOINT + Q_P_KEY,
                        "message": message,
                        "headers": headers,
                    },
                )
                thread.start()
                return jsonify(
                    {
                        "message": "First API call did not succeed, persistent calling in the background in progress.",
                        "next": "Call /delayed_response later to get the valid response (when available) of this call.",
                    }
                )

        except Exception as e:
            raise e


class DelayedResponseProvider(Resource):
    """Provides delayed response of last call for /crypto/sign endpoint if stored and available in the msg_store."""

    def get(self) -> Response:
        from models import Records
        from schema import message_schema

        args = request.args
        message = str(args["message"])
        try:
            returnable_q = Records.query.filter_by(message=message).first()
            return (
                message_schema.dump(returnable_q).get("signed_message")
                if returnable_q
                else jsonify("The result is not available yet.")
            )
        except KeyError:
            return jsonify("signed message not available yet, try again later.")
