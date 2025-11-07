import requests
import logging


class WebODMAPI:
    # These permission groups are Django identifiers for WebODM permission types
    # They're not properly documented. I learned the IDs by
    # * manually editing one user to add the permissions I'd like
    # * learning that user's numeric ID by looking at the URL in the admin UI
    # * making an API query for that user ID (see get_user method) to read the list
    permission_groups = [33, 34, 35, 36, 37, 38, 39, 40, 49, 50, 51, 52, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]

    def __init__(self, baseurl: str = "http://localhost:8000"):
        self.baseurl = baseurl
        self._token = None

    def auth_headers(self):
        token = self.read_token()
        return {"Authorization": f"JWT {token}", "Content-type": "application/json"}

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

    def create_user(
        self, username: str, password: str, groups: list = [], permissions: list = []
    ):
        """Creates a new WebODM user with the name passed in
        /api/admin/users/{id}/
        """
        if not len(permissions):
            permissions = self.permission_groups

        params = {
            "username": username,
            "password": password,
            "groups": groups,
            "user_permissions": permissions,
        }

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
        if response.status_code == 404:
            raise Exception(response.content)

        return response

    def get_user(self, userid: int):
        """read a user's details
        /api/admin/users/{id}/
        """

        url = self.baseurl + f"/api/admin/users/{userid}/"

        try:
            response = requests.get(url, headers=self.auth_headers())

        except Exception as err:
            logging.error(err)
            raise (err)

        assert response.status_code == 200
        return response.json()

    def groups(self):
        """read a list of groups
        /api/admin/users/{id}/
        """

        url = self.baseurl + "/api/admin/groups/"

        try:
            response = requests.get(url, headers=self.auth_headers())

        except Exception as err:
            logging.error(err)
            raise (err)

        assert response.status_code == 200
        return response.json()
