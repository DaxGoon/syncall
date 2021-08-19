import unittest
import requests

from app import app, db
from resources import API_KEY, Q_P_KEY

BASE_URL = "http://127.0.0.1:5000"
MSG = str("Test message")
HEADERS = {"Content-Type": "application/json", "Authorization": API_KEY}


class TestApi(unittest.TestCase):
    """ Test all application modules."""

    def setUp(self) -> None:
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        self.assertEqual(app.debug, False)

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def test_message_sign_connector_success_status_code(self) -> None:
        res = requests.get(
            BASE_URL + "/crypto/sign" + Q_P_KEY + MSG, headers=HEADERS, timeout=2
        )
        self.assertEqual(res.status_code, 200, msg="status code 200")

    def test_message_sign_connector_response_available(self) -> None:
        res = requests.get(
            BASE_URL + "/crypto/sign" + Q_P_KEY + MSG, headers=HEADERS, timeout=2
        )
        if res.text:
            self.assertEqual(type(res.text), str, msg="signed string")

    def test_message_sign_connector_response_unavailable(self) -> None:
        res = requests.get(
            BASE_URL + "/crypto/sign" + Q_P_KEY + MSG, headers=HEADERS, timeout=2
        )
        if not res.text:
            self.assertEqual(type(res.json()), dict)

    def test_delayed_response_provider_status_code(self) -> None:
        res = requests.get(
            BASE_URL + "/delayed_response" + Q_P_KEY + MSG, headers=HEADERS, timeout=2
        )
        self.assertEqual(res.status_code, 200, msg="status code 200")

    def test_delayed_response_provider_response_type(self) -> None:
        res = requests.get(
            BASE_URL + "/delayed_response" + Q_P_KEY + MSG, headers=HEADERS, timeout=2
        )
        self.assertEqual(type(res.text), str)


if __name__ == "__main__":
    unittest.main()
