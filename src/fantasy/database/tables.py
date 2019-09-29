from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import func
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

if __name__ == "__main__":
	database = "fantasy_football_2019"
	con = create_engine("mysql+mysqldb://root:@localhost/{database}".format(database=database))
	metadata.create_all(con)
