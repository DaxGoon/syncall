import requests
from requests.exceptions import HTTPError
from flask import request, Response
from flask_restful import Resource

from config import Config

SYNTHESIA_ENDPOINT = Config.synthesia_api_endpoint
Q_P_KEY = Config.synthesia_api_sign_query_param_key
API_KEY = Config.synthesia_api_key


class MessageSignConnector(Resource):
    """
    Represent Synthesia API's Sign service by accepting and forwarding calls to it and returning either a valid response
     if available or a custom response with useful information to the client.
    """

    def get(self, message):

        message = request.form["message"]

        try:
            res = requests.get(
                SYNTHESIA_ENDPOINT + Q_P_KEY + message,
                headers={"Authorization": API_KEY}
            )

            res.raise_for_status()
            return Response(
                res.json(), status=res.status_code, content_type=res.headers["content-type"]
            )
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
