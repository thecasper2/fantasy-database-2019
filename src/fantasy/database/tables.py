from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table


metadata = MetaData()
teams = Table(
	"teams",
	metadata,
	Column("code", Integer),
	Column("draw", Integer),
	Column("form", String(50)),
	Column("id", Integer, primary_key=True),
	Column("loss", Integer),
	Column("name", String(50)),
	Column("played", Integer),
	Column("points", Integer),
	Column("position", Integer),
	Column("short_name", String(50)),
	Column("strength", Integer),
	Column("team_division", String(50)),
	Column("unavailable", Boolean),
	Column("win", Integer),
	Column("strength_overall_home", Integer),
	Column("strength_overall_away", Integer),
	Column("strength_attack_home", Integer),
	Column("strength_attack_away", Integer),
	Column("strength_defence_home", Integer),
	Column("strength_defence_away", Integer),
)

players = Table(
	"players",
	metadata,
	Column("chance_of_playing_next_round", Float),
	Column("chance_of_playing_this_round", Float),
	Column("code", Integer),
	Column("cost_change_event", Integer),
	Column("cost_change_event_fall", Integer),
	Column("cost_change_start", Integer),
	Column("cost_change_start_fall", Integer),
	Column("dreamteam_count", Integer),
	Column("element_type", Integer),
	Column("ep_next", Float),
	Column("ep_this", Float),
	Column("event_points", Integer),
	Column("first_name", String(50)),
	Column("form", Float),
	Column("id", Integer, primary_key=True),
	Column("in_dreamteam", Boolean),
	Column("news", String(200)),
	Column("news_added", String(50)),
	Column("now_cost", Integer),
	Column("photo", String(50)),
	Column("points_per_game", Float),
	Column("second_name", String(50)),
	Column("selected_by_percent", Float),
	Column("special", Boolean),
	Column("squad_number", String(50)),
	Column("status", String(50)),
	Column("team", Integer, ForeignKey("teams.id")),
	Column("team_code", Integer),
	Column("total_points", Integer),
	Column("transfers_in", Integer),
	Column("transfers_in_event", Integer),
	Column("transfers_out", Integer),
	Column("transfers_out_event", Integer),
	Column("value_form", Float),
	Column("value_season", Float),
	Column("web_name", String(50)),
	Column("minutes", Integer),
	Column("goals_scored", Integer),
	Column("assists", Integer),
	Column("clean_sheets", Integer),
	Column("goals_conceded", Integer),
	Column("own_goals", Integer),
	Column("penalties_saved", Integer),
	Column("penalties_missed", Integer),
	Column("yellow_cards", Integer),
	Column("red_cards", Integer),
	Column("saves", Integer),
	Column("bonus", Integer),
	Column("bps", Integer),
	Column("influence", Float),
	Column("creativity", Float),
	Column("threat", Float),
	Column("ict_index", Float),
)

player_history = Table(
	"player_history",
	metadata,
	Column("element", Integer, primary_key=True),
	Column("fixture", Integer, primary_key=True),
	Column("opponent_team", Integer),
	Column("total_points", Integer),
	Column("was_home", Boolean),
	Column("kickoff_time", String(200)),
	Column("team_h_score", Float),
	Column("team_a_score", Float),
	Column("round", Integer),
	Column("minutes", Integer),
	Column("goals_scored", Integer),
	Column("assists", Integer),
	Column("clean_sheets", Integer),
	Column("goals_conceded", Integer),
	Column("own_goals", Integer),
	Column("penalties_saved", Integer),
	Column("penalties_missed", Integer),
	Column("yellow_cards", Integer),
	Column("red_cards", Integer),
	Column("saves", Integer),
	Column("bonus", Integer),
	Column("bps", Integer),
	Column("influence", Float),
	Column("creativity", Float),
	Column("threat", Float),
	Column("ict_index", Float),
	Column("value", Integer),
	Column("transfers_balance", Integer),
	Column("selected", Integer),
	Column("transfers_in", Integer),
	Column("transfers_out", Integer),
)

if __name__ == "__main__":
	"""
	If this script is invoked directly, it will create all the tables in a MySQL database at localhost, with
	a database name as set below. A MySQL server must be running for this to work.
	"""
	database = "fantasy_football_2019"
	con = create_engine("mysql+mysqldb://root:@localhost/{database}".format(database=database))
	metadata.create_all(con)
