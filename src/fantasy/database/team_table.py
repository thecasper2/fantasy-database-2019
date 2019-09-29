from .base_table import BaseTable
from .tables import teams
from src.fantasy.api.bootstrap_static_api import BootstrapStaticAPI


class TeamTable(BaseTable):
	"""
	A class for performing methods on the team table
	"""

	def __init__(self):
		"""
		We take the content from the API teams response
		"""
		super(TeamTable, self).__init__(
			table=teams,
			content=BootstrapStaticAPI().content["teams"]
		)
