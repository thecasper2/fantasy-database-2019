from .base_api import BaseAPI
from .apis import api_dict


class BootstrapStaticAPI(BaseAPI):
	"""
	API that contains the following subdirs:
		events: Fantasy Football game weeks
		game_settings:
		phases:
		teams: a list of Premier League teams
		total_players:
		elements: a list of Premier League players and summary stats at the current time
		element_stats:
	"""

	def __init__(self, class_name: str = "bootstrap_static"):
		"""
		Using the class name, extract the relevant dict entry for this API
		"""
		super(BootstrapStaticAPI, self).__init__(class_name)
