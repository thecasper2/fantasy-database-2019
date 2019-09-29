from json import loads
from requests import get

from .apis import api_dict


class BaseAPI(object):
	"""
	Base class for APIs
	"""

	def __init__(self, class_name: str, player_id: int = None):
		"""
		We take the class name and extract the API URL from the api_dict. We then note the GET response from that URL
		and if it isn't 200, we raise an error
		:param class_name: The name of the class, used to look up the API in the api_dict
		"""
		self.api = api_dict[class_name]
		self.response = get(self.api["url"].format(player_id=player_id))
		self.content = loads(self.response.content)
