import json

import requests
from flask import jsonify
from flask_restful import request, Resource

from config import Config

SYNTHESIA_ENDPOINT = Config.synthesia_api_endpoint
Q_P_KEY = Config.synthesia_api_sign_query_param_key
API_KEY = Config.synthesia_api_key


class MessageSignConnector(Resource):
    """
    Represent Synthesia API's Sign service by accepting and forwarding calls to it and returning either a valid response
     if available or a custom response with useful information to the client.
    """

    def get(self):

        args = request.args
        message = str(args["message"])
        headers = {
            'Content-Type': 'application/json',
            "Authorization": API_KEY
        }
        try:
            res = requests.get(
                SYNTHESIA_ENDPOINT + Q_P_KEY + message,
                headers=headers,
                timeout=2
            )

            return res.text if res.ok else jsonify(
                {"request_status": "failed",
                 "reason": res.reason,
                 "returned_status_code": res.status_code
                 }
            )

        except Exception as e:
            raise e
