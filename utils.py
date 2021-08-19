from time import sleep
from typing import Any

import requests
from flask_socketio import emit


def keep_calling_on_failure(**kwargs: Any) -> None:
    """
    Calls the api endpoint (full uri) and stores when a valid response is received.
    :param kwargs: API request params.
    :return: None
    """
    from app import db
    from models import Records

    full_uri = kwargs.get("full_uri", {})
    message = kwargs.get("message", {})
    headers = kwargs.get("headers", {})

    for _ in range(100):
        res = requests.get(full_uri + message, headers=headers)
        if res.ok:
            broadcast_notification_via_socket(message)
            try:
                new_record = Records(message=message, signed_message=res.text)
                db.session.add(new_record)
                db.session.commit()
            except Exception as e:
                print(e)
            break
        sleep(6)


def broadcast_notification_via_socket(data: Any) -> None:
    """Broadcast notification with SocketIO."""
    from app import socketio

    @socketio.on("event")
    def handle_my_custom_event(d: Any = data) -> None:
        emit("signed msg available for: ", d, broadcast=True)
