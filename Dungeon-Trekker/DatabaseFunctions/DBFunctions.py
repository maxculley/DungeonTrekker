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
	for data in myresult:
		dumpTweets.append(data[0])
	return dumpTweets


def updateMentions(mentions):
	finalList = []
	dumpTweetList = getDumpTweets()
	dumpTweetsSet = set()

	for tweet in dumpTweetList:
		dumpTweetsSet.add(str(tweet))


	for mention in mentions:
		if str(mention.id) in dumpTweetsSet:
			break
		else:
			finalList.append(mention)
			executeUpdate("INSERT INTO Tweet_dump VALUES(" + str(mention.id) + ", " + str(mention.user.id) + ");")

	return finalList


def getSavedUsers():
	finalUsers = set()
	users = executeMultipleQuery("SELECT user_id FROM Users")

	for user in users:
		finalUsers.add(user[0])

	return finalUsers


def addUser(currentMentionsList):
	mentionsUserIDList = []
	count = 0

	for mention in currentMentionsList:
		mentionsUserIDList.append(str(mention.user.id))

	for mention in mentionsUserIDList:
		userList = getSavedUsers()
		if mention in userList:
			pass
		else:
			executeUpdate("INSERT INTO Users VALUES(" + str(mention) + ", '" + str(((api.get_user(mention)).name)) + "', '@" + str(((api.get_user(mention)).screen_name)) + "');")
		count += 1
