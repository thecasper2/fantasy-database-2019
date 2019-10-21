from sys import stdout

from src.fantasy.database.team_table import TeamTable
from src.fantasy.database.player_table import PlayerTable
from src.fantasy.database.player_history_table import PlayerHistoryTable


if __name__ == "__main__":
	"""
	If this script is invoked directly, it will create an instance of each table class, then call the update_table
	method on each to write to MySQL
	"""
	stdout.write("Updating team table")
	TeamTable().update_table()
	stdout.write("Updating player table")
	PlayerTable().update_table()
	stdout.write("Updating player history table")
	PlayerHistoryTable().update_table()
