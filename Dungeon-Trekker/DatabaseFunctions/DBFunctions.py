from Connections.twitterAccess import *
from Connections.dbConnection import *

cursor = getCursor()
myresult = None
myresultFinal = []
count = 0 # Used to access the tweet ID's
updatedList = []


def executeUpdate(query):
	cursor.execute(query)
	getMydb().commit()

def executeSingleQuery(query):
	cursor.execute(query)
	myresult = cursor.fetchone()
	myresultFinal = myresult[0]
	return myresultFinal

def executeMultipleQuery(query):
	cursor.execute(query)
	myresult = cursor.fetchall()
	return myresult

def getDumpTweets():
	dumpTweets = []
	myresult = executeMultipleQuery("SELECT tweet_id FROM Tweet_dump")
	for x in myresult:
		dumpTweets.append(x[0])
	return dumpTweets


def updateMentions(mentions):
	dumpTweetList = []
	finalList = []
	dumpListLength = None

	dumpTweetList = getDumpTweets()
	dumpListLength = len(dumpTweetList)

	for x in mentions:
		counter = 0
		for y in dumpTweetList:
			counter += 1
			if str(x.id) == str(y):
				break
			elif counter == dumpListLength:
				finalList.append(x)
				executeUpdate("INSERT INTO Tweet_dump VALUES(" + str(x.id) + ");")
			else:
				pass
	
	return finalList