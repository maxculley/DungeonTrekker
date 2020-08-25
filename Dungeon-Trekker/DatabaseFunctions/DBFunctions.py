from Connections.twitterAccess import *
from Connections.dbConnection import *
from Rooms.Rooms import *

import tweepy

api = getAPI()
cursor = getCursor()
myresult = None

############## Execute Queries ##############

def executeUpdate(query):
	cursor.execute(query)
	getMydb().commit()

def executeSingleQuery(query):
	cursor.execute(query)
	myresult = cursor.fetchone()
	return myresult

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
		dumpTweetsSet.add(str(tweet)) # Add each tweet into a set


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


def addUser(mentions):
	mentionsUserIDList = []
	userList = getSavedUsers()

	for mention in mentions:
		mentionsUserIDList.append(str(mention.user.id))

	for mention in mentionsUserIDList:
		if mention in userList:
			pass
		else:
			executeUpdate("INSERT INTO Users VALUES(" + str(mention) + ", '" + str(((api.get_user(mention)).name)) + "', '@" + str(((api.get_user(mention)).screen_name)) + "');")


############## Database Refresh ##############



def refreshDBTweets():
	tweetList = getDumpTweets()

	for tweet in tweetList:
		tempList = []
		tempList.append(tweet)
		tempObj = api.statuses_lookup(tempList)
		if len(tempObj) == 0:
			executeUpdate("DELETE FROM Tweet_dump WHERE tweet_id = " + str(tweet) + ";")
		else:
			pass


############## Database Check ##############



def checkUserGame(userID):
	isUser = None
	isUser = executeSingleQuery("SELECT user_id FROM Users WHERE user_id = " + str(userID) + ";")

	if isUser == None:
		return False
	else:
		return True


def createGame(tweet, hasGame):
	if hasGame == True:
		executeUpdate("UPDATE User_games SET current_room_id= 1, current_code= 0, current_riddle= 0 WHERE user_id= " + str(tweet.user.id) + ";")
	else:
		executeUpdate("INSERT INTO User_games VALUES(" + str(tweet.user.id) + ", 1, 0, 0);")


def decideRoom(tweet):
	currentRoom = executeSingleQuery("SELECT current_room_id FROM User_games WHERE user_id= " + str(tweet.user.id) + ";")
	currentRoom = currentRoom[0]

	if currentRoom == "1":
		room1(tweet)









