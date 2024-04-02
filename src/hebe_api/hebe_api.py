import requests
import json
from urllib.parse import urlencode


class Hebe:
    NO_TOKEN = "Use hebe.authenticate() in order to obtain the token"

    def __init__(self, username: str = "", password: str = "") -> None:
        self.username = username
        self.password = password
        self.token = None

    def authenticate(self, username: str = "", password: str = "") -> None:
        if username != "":
            self.username = username
        if password != "":
            self.password = password
        initial_token, csrf_token = self._get_initial_token()
        self.token = self._authenticate(initial_token, csrf_token)

    def _authenticate(self, initial_token: str, csrf_token: str) -> str:
        url = (
            "https://www.hebe.pl/on/demandware.store/Sites-Hebe-Site"
            "/pl_PL/Login-LoginForm"
        )
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://www.hebe.pl",
            "Referer": "https://www.hebe.pl/home?showform=true"
            "&targeturl=%2Faccount",
            "Cookie": f"dwsid={initial_token};",
        }
        body = urlencode(
            {
                "dwfrm_login_username_d0uexrwjfbur": self.username,
                "dwfrm_login_password_d0vyhxgwmmwx": self.password,
                "csrf_token": csrf_token,
                "dwfrm_login_login": "",
                "format": "ajax",
            }
        )
        response = requests.post(url=url, headers=headers, data=body)
        response_data = json.loads(response.text)
        if "error" in response_data:
            raise Exception(f"Authentication failed: {response_data['error']}")
        elif (
            "status" not in response_data
            or response_data["status"] != "SUCCESS"
        ):
            raise Exception(
                "Authentication failed: lack of 'status'='SUCCESS' flag"
                "in authenticate response body"
            )
        header = response.headers["Set-Cookie"]
        if "dwsid=" not in header:
            raise Exception(
                "dwsid cookie is not present in the final token retrieval"
            )
        dwsid = header.split("dwsid=")[1].split(";")[0]
        if not dwsid:
            raise Exception(
                "dwsid cookie missing. Please contact the "
                "author of the lib for resolution"
            )
        return dwsid

    def get_orders(self):
        if self.token is None:
            raise Exception(self.NO_TOKEN)

    def _get_initial_token(self) -> tuple[str, str]:
        response = requests.get("https://www.hebe.pl")
        header = response.headers["Set-Cookie"]
        if "dwsid=" not in header:
            raise Exception(
                "dwsid cookie is not present in the initial token retrieval"
            )
        dwsid = header.split("dwsid=")[1].split(";")[0]
        if not dwsid:
            raise Exception(
                "dwsid cookie missing. Please contact the "
                "author of the lib for resolution"
            )
        csrf_json = json.loads(
            response.text.split("window.CSRFToken = ")[1].split(";")[0]
        )
        csrf_token = csrf_json["value"]
        return dwsid, csrf_token
