from tqdm import tqdm

from .base_table import BaseTable
from .tables import player_history
from src.fantasy.api.bootstrap_static_api import BootstrapStaticAPI
from src.fantasy.api.player_history_api import PlayerHistoryAPI


class PlayerHistoryTable(BaseTable):
	"""
	A class for performing methods on the team table
	"""

	def __init__(self, from_round: int = 1):
		"""
		Firstly we get all player ID values from the Bootstrap static API. We then fire a request to the history API
		for each player ID and bind the result to make a very large data frame of player history.
		from_round: Limit the results to any fixtures in or above this round
		"""
		bootstrap = BootstrapStaticAPI()
		player_ids = bootstrap.player_ids()
		player_history_data = []
		for player_id in tqdm(player_ids):
			player_history_data.extend(PlayerHistoryAPI(player_id=player_id).history())
		super(PlayerHistoryTable, self).__init__(
			table=player_history,
			content=player_history_data
		)
		self.content = [c for c in self.content if c["round"] >= from_round]
