from sqlalchemy import create_engine


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

	def update_table(self):
		"""
		Deletes all data from a table, and inserts new content
		TODO: This should be done with an on duplicate key update statement, but I can't work it out
		"""
		con = self.database_connection()
		ins = self.table.insert()
		con.execute(self.table.delete())
		con.execute(ins, self.content)
		con.dispose()
