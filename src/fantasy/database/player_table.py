from .base_table import BaseTable
from .tables import players
from src.fantasy.api.bootstrap_static_api import BootstrapStaticAPI


class PlayerTable(BaseTable):
	"""
	A class for performing methods on the team table
	"""

	def __init__(self):
		"""
		We take the content from the API teams response
		"""
		super(PlayerTable, self).__init__(
			table=players,
			content=BootstrapStaticAPI().content["elements"]
		)
