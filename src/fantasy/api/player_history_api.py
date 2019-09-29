from .base_api import BaseAPI


class PlayerHistoryAPI(BaseAPI):
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

	def __init__(self, class_name: str = "player_history", player_id: int = 1):
		"""
		Using the class name and player ID, extract the relevant dict entry for this API
		:param class_name: The name of the class to look up in the API dict
		:param player_id: The player ID for which we make the request
		"""
		super(PlayerHistoryAPI, self).__init__(class_name, player_id)
