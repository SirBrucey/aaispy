import json
import requests

BASE_URL = "https://chaos.aa.net.uk/"

class Chaos(object):
    """This class allows access to the Andrews & Arnold API.

    Note that it is based on trial and error, there is very little
    official documentation about this API yet, so use at your own risk.
    """

    def __init__(self, username, password):
        """Initialize the class.

        Use the same credentials as on control.aa.net.uk.

        Args:
            username: username like xx00@x
            password: self-explanatory
        """
        self.session = requests.session()
        self.session.headers["User-Agent"] = "Python Chaos Client"
        self.session.auth = (username, password)

    def _request(self, **kwargs):
        """Make an API request, lets Requests check the HTTP status code
        then checks if the "error" string is present in the response
        and raises an exception if that's the case.

        Args:
            **kwargs: will be passed as-is to python-requests
        Returns:
            a dict representation of the APi'S JSON reply
        Raises:
            Exception: the remote server returned an error
        """

        resp = self.session.post(BASE_URL, **kwargs)

        if resp.status_code != requests.codes.ok:
            resp.raise_for_status()

        resp = resp.json()
        
        if "error" in resp:
            raise APIError(resp["error"])

        return resp

    def info(self, **kwargs):
        return self._request(json={**kwargs, **{"command": "info"}})

    def change(self, **kwargs):
        required = ["broadband", "sim", "voip"]

        if not any(arg in required for arg in kwargs):
            raise InvalidParameters("Missing object of types: " + ", ".join(required))

        return self._request(json={**kwargs, **{"command": "change"}})

    def check(self, **kwargs):
        required = ["order"]

        if not any(arg in required for arg in kwargs):
            raise InvalidParameters("Missing object of types: " + ", ".join(required))

        return self._request(json={**kwargs, **{"command": "check"}})

    def preorder(self, **kwargs):
        required = ["order"]

        if not any(arg in required for arg in kwargs):
            raise InvalidParameters("Missing object of types: " + ", ".join(required))

        return self._request(json={**kwargs, **{"command": "preorder"}})

    def order(self, **kwargs):
        required = ["order"]

        if not any(arg in required for arg in kwargs):
            raise InvalidParameters("Missing object of types: " + ", ".join(required))

        return self._request(json={**kwargs, **{"command": "order"}})

    def usage(self, **kwargs):
        required =  ["broadband", "sim", "voip"]

        if not any(arg in required for arg in kwargs):
            raise InvalidParameters("Missing object of types: " + ", ".join(allowed))

        return self._request(json={**kwargs, **{"command": "usage"}})

    def availability(self, **kwargs):
        required = ["broadband"]

        if not any(arg in required for arg in kwargs):
            raise InvalidParameters("Missing object of types: " + ", ".join(required))

        return self._request(json={**kwargs, **{"command": "availability"}})

class ChaosException(Exception):
    """Base class for all our exceptions.
    """
    pass

class InvalidParameters(ChaosException):
    """Indicates a problem with the request's arguments.
    """
    pass

class APIError(ChaosException):
    """Indicates an error returned by the remote server.
    """
    pass