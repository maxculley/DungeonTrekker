from Connections.twitterAccess import *
from Connections.dbConnection import *

cursor = getCursor()

def executeQuery(query):
	cursor.execute(query)
	getMydb().commit()