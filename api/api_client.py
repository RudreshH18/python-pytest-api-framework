import requests


class APIClient:
    """
    Reusable API client to handle HTTP requests
    """

    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.timeout = timeout

    def get(self, endpoint, headers=None):
        return requests.get(
            self.base_url + endpoint,
            headers=headers,
            timeout=self.timeout
        )

    def post(self, endpoint, json=None, headers=None):
        return requests.post(
            self.base_url + endpoint,
            json=json,
            headers=headers,
            timeout=self.timeout
        )

    def put(self, endpoint, json=None, headers=None):
        return requests.put(
            self.base_url + endpoint,
            json=json,
            headers=headers,
            timeout=self.timeout
        )

    def delete(self, endpoint, headers=None):
        return requests.delete(
            self.base_url + endpoint,
            headers=headers,
            timeout=self.timeout
        )

