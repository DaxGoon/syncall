from time import sleep
from typing import Any

import requests

from contemporary_storage import contemporary_storage


def keep_calling_on_failure(**kwargs: Any) -> None:
    """
    Calls the api endpoint (full uri) and stores when a valid response is received.
    :param kwargs: API request params.
    :return: None
    """
    full_uri = kwargs.get("full_uri", {})
    message = kwargs.get("message", {})
    headers = kwargs.get("headers", {})

    for _ in range(100):
        res = requests.get(full_uri + message, headers=headers)
        if res.ok:
            contemporary_storage[message] = res.text
            break
        sleep(6)
