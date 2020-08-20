from Connections.twitterAccess import *
from Connections.dbConnection import *

import tweepy

api = getAPI()
cursor = getCursor()
myresult = None
myresultFinal = []
count = 0 # Used to access the tweet ID's
updatedList = []

############## Execute Queries ##############

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


##############  ##############


def getDumpTweets():
	dumpTweets = []

	myresult = executeMultipleQuery("SELECT tweet_id FROM Tweet_dump")
	for x in myresult:
		dumpTweets.append(x[0])
	return dumpTweets


def updateMentions(mentions):
	finalList = []
	dumpTweetList = getDumpTweets()
	dumpTweetsSet = set()

	for x in dumpTweetList:
		dumpTweetsSet.add(str(x))


	for x in mentions:
		if str(x.id) in dumpTweetsSet:
			break
		else:
			finalList.append(x)
			executeUpdate("INSERT INTO Tweet_dump VALUES(" + str(x.id) + ", " + str(x.user.id) + ");")

	return finalList


def getSavedUsers():
	finalUsers = set()
	users = executeMultipleQuery("SELECT user_id FROM Users")

	for x in users:
		finalUsers.add(x[0])

	return finalUsers


def addUser(currentMentionsList):
	mentionsUserIDList = []
	count = 0

	for x in currentMentionsList:
		mentionsUserIDList.append(str(x.user.id))

	for x in mentionsUserIDList:
		userList = getSavedUsers()
		if x in userList:
			pass
		else:
			executeUpdate("INSERT INTO Users VALUES(" + str(x) + ", '" + str(((api.get_user(x)).name)) + "', '@" + str(((api.get_user(x)).screen_name)) + "');")
		count += 1
