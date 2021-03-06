from Connections.twitterAccess import *
from Connections.dbConnection import *
from DatabaseFunctions.DBFunctions import *
from TweepyFunctions.TweepyFunctions import *
from GeneralFunctions.GeneralFunctions import *

import tweepy
import time

api = getAPI() 
finalMentions = None # List of tweets that havent been replied to
a = 0
users = []

while(True):

	time.sleep(12)

	refreshDBTweets() # Clean database
	finalMentions = getFinalMentions() # Get all final tweets
	totalUsers = getUserCount()

	for tweet in finalMentions:
		text = (tweet.text).lower() # Turn the tweet text lowercase
		text = text.split(" ", 1)[1] # Get the content of the tweet

		hasGame = checkUserGame(tweet.user.id) # Check if the user already has a game

		if hasGame == False:
			createGame(tweet, False)
			howToPlay(tweet)

		currentRoom = getCurrentRoom(tweet) # Get current room

		currentCodeTemp = executeSingleQuery("SELECT current_code FROM User_games WHERE user_id = " + str(tweet.user.id) + "")
		currentCode = currentCodeTemp[0]

		currentRiddleTemp = executeSingleQuery("SELECT current_riddle FROM User_games WHERE user_id = " + str(tweet.user.id) + "")
		currentRiddle = currentRiddleTemp[0]


		print("Tweet text: " + text)

		if text == "start":
			decideRoom(tweet)

		elif text == "resume":
			decideRoom(tweet)

		elif text == "new":
			createGame(tweet, hasGame)
			decideRoom(tweet)

		elif text == "commands":
			commands(tweet)

		elif text == "help":
			help(tweet)
			favourite(tweet)

		elif text == "stats" and str(tweet.user.id) == "759343803723608064":
			stats(tweet, totalUsers)

		elif text == "stop" and str(tweet.user.id) == "759343803723608064":
			exit()

		elif text == "how to play":
			howToPlay()

		elif currentRoom == "8":
			if text == currentCode:
				codeCorrect(tweet, 9)
			else:
				incorrectCode(tweet)

		elif currentRoom == "28":
			if text == currentRiddle:
				riddleCorrect(tweet, 29)
			else:
				incorrectRiddle(tweet)

		elif currentRoom == "49":
			if text == currentCode:
				codeCorrect(tweet, 50)
			else:
				incorrectCode(tweet)

		elif currentRoom == "50":
			if text == currentRiddle:
				riddleCorrect(tweet, 51)
			else:
				incorrectRiddle(tweet)

		elif currentRoom == "51":
			decideRoom(tweet)

		elif "forward" in text:
			if hasGame == True:
				checkValidDirection(tweet, "forward")
			else:
				notRecognised(tweet)

		elif "back" in text:
			if hasGame == True:
				checkValidDirection(tweet, "back")
			else:
				notRecognised(tweet)

		elif "right" in text:
			if hasGame == True:
				checkValidDirection(tweet, "right")
			else:
				notRecognised(tweet)

		elif "left" in text:
			if hasGame == True:
				checkValidDirection(tweet, "left")
			else:
				notRecognised(tweet)

		elif "up" in text:
			if hasGame == True:
				checkValidDirection(tweet, "up")
			else:
				notRecognised(tweet)

		elif "down" in text:
			if hasGame == True:
				checkValidDirection(tweet, "down")
			else:
				notRecognised(tweet)

		elif "search" in text:
			if hasGame == True:
				checkValidDirection(tweet, "left")
			else:
				notRecognised(tweet)

		else:
			notRecognised(tweet)


	addUser(finalMentions) # Add new users to the database

	#a += 1