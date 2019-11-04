from sys import stdout

from src.fantasy.database.team_table import TeamTable
from src.fantasy.database.player_table import PlayerTable
from src.fantasy.database.player_history_table import PlayerHistoryTable


if __name__ == "__main__":
	"""
	If this script is invoked directly, it will create an instance of each table class, then call the update_table
	method on each to write to MySQL
	"""
	stdout.write("Updating team table\n")
	t = TeamTable()
	t.update_table()
	stdout.write("Updating player table\n")
	p = PlayerTable()
	p.update_table()
	stdout.write("Updating player history table\n")
	ph = PlayerHistoryTable()
	ph.update_table()
