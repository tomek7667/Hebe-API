import requests


class Hebe():
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
		initial_token = self._get_initial_token()
		print("Essor")


	def get_orders(self):
		if self.token is None:
			raise Exception("asd")
	
	def _get_initial_token(self) -> str:
		response = requests.get("https://www.hebe.pl")
		header = response.headers["Set-Cookie"]
		if "dwsid=" not in header:
			raise Exception("dwsid cookie is not present in the initial token retrieval")
		dwsid = header.split("dwsid=")[1].split(";")[0]
		if not dwsid:
			raise Exception("dwsid cookie missing. Please contact the author of the lib for resolution")
		return dwsid
		
	
