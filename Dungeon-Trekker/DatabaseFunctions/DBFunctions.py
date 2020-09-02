from Connections.twitterAccess import *
from Connections.dbConnection import *
from TweepyFunctions.TweepyFunctions import *
from Rooms.Rooms import *

import tweepy

api = getAPI()
cursor = getCursor()
cursor = getMydb().cursor(buffered=True)
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


############## Update Data ##############


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



############## User Methods ##############



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

def getUserCount():
	userList = executeMultipleQuery("SELECT user_id FROM Users")

	return len(userList)



############## Game Functions ##############



def createGame(tweet, hasGame):
	if hasGame == True:
		executeUpdate("UPDATE User_games SET current_room_id= 1, current_code= 0, current_riddle= 0 WHERE user_id= " + str(tweet.user.id) + ";")
	else:
		executeUpdate("INSERT INTO User_games VALUES(" + str(tweet.user.id) + ", 1, 0, 0);")


def getCurrentRoom(tweet):
	currentRoom = executeSingleQuery("SELECT current_room_id FROM User_games WHERE user_id= " + str(tweet.user.id) + ";")
	return currentRoom[0]


def decideRoom(tweet):
	currentRoom = getCurrentRoom(tweet)

	if currentRoom == "1":
		room1(tweet)

	elif currentRoom == "2":
		room2(tweet)

	elif currentRoom == "3":
		room3(tweet)

	elif currentRoom == "4":
		room4(tweet)

	elif currentRoom == "5":
		room5(tweet)

	elif currentRoom == "6":
		room6(tweet)
		addCodes(tweet)

	elif currentRoom == "7":
		room7(tweet)

	elif currentRoom == "8":
		room8(tweet)

	elif currentRoom == "9":
		room9(tweet)

	elif currentRoom == "10":
		room10(tweet)

	elif currentRoom == "11":
		room11(tweet)

	elif currentRoom == "12":
		room12(tweet)

	elif currentRoom == "13":
		room13(tweet)

	elif currentRoom == "14":
		room14(tweet)

	elif currentRoom == "15":
		room15(tweet)

	elif currentRoom == "16":
		room16(tweet)

	elif currentRoom == "17":
		room17(tweet)

	elif currentRoom == "18":
		room18(tweet)

	elif currentRoom == "19":
		room19(tweet)

	elif currentRoom == "20":
		room20(tweet)

	elif currentRoom == "21":
		room21(tweet)

	elif currentRoom == "22":
		room22(tweet)

	elif currentRoom == "23":
		room23(tweet)

	elif currentRoom == "24":
		room24(tweet)

	elif currentRoom == "25":
		room25(tweet)

	elif currentRoom == "26":
		room26(tweet)

	elif currentRoom == "27":
		room27(tweet)

	elif currentRoom == "28":
		room28(tweet)
		addCodes(tweet)

	elif currentRoom == "29":
		room29(tweet)

	elif currentRoom == "30":
		room30(tweet)

	elif currentRoom == "31":
		room31(tweet)

	elif currentRoom == "32":
		room32(tweet)

	elif currentRoom == "33":
		room33(tweet)

	elif currentRoom == "34":
		room34(tweet)

	elif currentRoom == "35":
		room35(tweet)

	elif currentRoom == "36":
		room36(tweet)

	elif currentRoom == "37":
		room37(tweet)

	elif currentRoom == "38":
		room38(tweet)

	elif currentRoom == "39":
		room39(tweet)

	elif currentRoom == "40":
		room40(tweet)

	elif currentRoom == "41":
		room41(tweet)

	elif currentRoom == "42":
		room42(tweet)

	elif currentRoom == "90":
		room90(tweet)

	elif currentRoom == "91":
		room91(tweet)



def updateRoom(tweet, newRoom):
	executeUpdate("UPDATE User_games SET current_room_id= " + str(newRoom) + " WHERE user_id= " + str(tweet.user.id) + "")


def checkValidDirection(tweet, direction):
	currentRoom = getCurrentRoom(tweet)
	directionValue = executeSingleQuery("SELECT `" + str(direction) + "` FROM Rooms WHERE room_id= " + str(currentRoom) + ";")
	directionValue = directionValue[0]


	if directionValue == "0":
		directionNotRecognised(tweet)
	else:
		updateRoom(tweet, directionValue)
		decideRoom(tweet)

def addCodes(tweet):
	currentRoom = getCurrentRoom(tweet)

	if currentRoom == "6":
		executeUpdate("UPDATE User_games SET current_code='rhyme' WHERE user_id = " + str(tweet.user.id) + "")
	elif currentRoom == "28":
		executeUpdate("UPDATE User_games SET current_riddle='fire' WHERE user_id = " + str(tweet.user.id) + "")


def codeCorrect(tweet, newRoomID):
	updateRoom(tweet, newRoomID)
	executeUpdate("UPDATE User_games SET current_code='0' WHERE user_id = " + str(tweet.user.id) + "")
	decideRoom(tweet)

def riddleCorrect(tweet, newRoomID):
	updateRoom(tweet, newRoomID)
	executeUpdate("UPDATE User_games SET current_riddle='0' WHERE user_id = " + str(tweet.user.id) + "")
	decideRoom(tweet)



