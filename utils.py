from time import sleep
import requests
from contemporary_storage import contemporary_storage


def keep_calling_on_failure(**kwargs):
    full_uri = kwargs.get("full_uri", {})
    message = kwargs.get("message", {})
    headers = kwargs.get("headers", {})

    for _ in range(100):
        res = requests.get(full_uri + message, headers=headers)
        if res.ok:
            contemporary_storage[message] = res.text
            break
        sleep(6)
