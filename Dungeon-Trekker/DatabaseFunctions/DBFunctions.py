from Connections.twitterAccess import *
from Connections.dbConnection import *

cursor = getCursor()
myresult = None
myresultFinal = None


def executeUpdate(query):
	cursor.execute(query)
	getMydb().commit()

def executeSingleQuery(query):
	cursor.execute(query)
	myresult = cursor.fetchone()
	myresultFinal = myresult[0]
	return myresultFinal

def checkMentions(mentions):
	result = executeSingleQuery("SELECT latest_mention_id FROM General")
	newMentions = []

	for x in mentions:
		if (str(x.id) == str(result)) == True:
			break
		else:
			newMentions.insert(0, x.id)

	return newMentions