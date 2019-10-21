from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.dialects.mysql import insert


class BaseTable(object):
	"""
	Base class for MySQL tables
	"""

	def __init__(self, table, content, database_name: str = "fantasy_football_2019"):
		"""
		We create the base table class with a database name
		:param table: The sqlalchemy table definition
		:param content: Some content that can be written to the table
		:param database_name: The name of the database
		"""
		self.database_name = database_name
		self.table = table
		self.content = content

	def database_connection(self):
		"""
		Gets a database connection dependent on the database name
		:return: A database connection
		"""
		return create_engine("mysql+mysqldb://root:@localhost/{database}".format(database=self.database_name))

	def update_table(self, upsert: bool=True):
		"""
		Deletes all data from a table, and inserts new content
		TODO: This should be done with an on duplicate key update statement, but I can't work it out
		"""
		con = self.database_connection()
		insert_stmt = insert(self.table).values(self.content)
		if upsert:
			upsert_vals = {k: insert_stmt.inserted[k] for k, v in self.content[0].items()}
			upsert_vals.update({"updated_at": func.current_timestamp()})
			insert_stmt = insert_stmt.on_duplicate_key_update(
				upsert_vals
			)
		con.execute(insert_stmt, self.content)
		con.dispose()
