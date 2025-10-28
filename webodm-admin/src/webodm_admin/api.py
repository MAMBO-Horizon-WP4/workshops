import requests
import logging


class WebODMAPI:
    def __init__(self, baseurl: str = "http://localhost:8000"):
        self.baseurl = baseurl
        self._token = None

    def auth_headers(self):
        token = self.read_token()
        return {"Authorization": f"JWT {token}"}

    def read_token(self):
        if not self._token:
            with open(".token", "r") as input:
                self._token = input.read()

        return self._token

    def auth_token(self, username: str, password: str):
        """
        Make a request for an authentication token (as an admin)
        curl -X POST -d "username=testuser&password=testpass" http://localhost:8000/api/token-auth/

        Returns a dict that looks like this
        {"token":"eyJ0eXAiO..."}
        """
        params = {"username": username, "password": password}
        try:
            response = requests.post(self.baseurl + "/api/token-auth/", json=params)
        except Exception as err:
            logging.error(err)
            raise (err)

        assert response.status_code == 200
        # Write a token to reuse. It expires after 6 hours
        token = response.json()["token"]
        with open(".token", "w") as out:
            out.write(token)

        return token

    def create_user(self, username: str, password: str, groups: list = []):
        """Creates a new WebODM user with the name passed in
        /api/admin/users/{id}/
        """

        params = {"username": username, "password": password, "groups": groups}
        url = self.baseurl + "/api/admin/users/"
        try:
            response = requests.post(url, json=params, headers=self.auth_headers())
        except Exception as err:
            logging.error(err)
            raise (err)

        if (
            response.status_code == 400
            and "already exists" in response.json()["username"]
        ):
            return

        return response
