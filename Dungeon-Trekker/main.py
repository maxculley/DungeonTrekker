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

while(a < 1):

	#time.sleep(12)

	refreshDBTweets() # Clean database
	finalMentions = getFinalMentions() # Get all final tweets

	for tweet in finalMentions:
		text = (tweet.text).lower() # Turn the tweet text lowercase
		text = text.split(" ", 1)[1] # Get the content of the tweet
		hasGame = checkUserGame(tweet.user.id)

		print("Tweet text: " + text)

		if text == "start":
			result = checkUserGame(tweet.user.id)
			if result == True:
				resume(tweet)
			else:
				createGame(tweet, False)
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

		elif "forward" in text:
			checkValidDirection(tweet, "forward")

		elif "back" in text:
			checkValidDirection(tweet, "back")

		elif "right" in text:
			checkValidDirection(tweet, "right")

		elif "left" in text:
			checkValidDirection(tweet, "left")

		elif "up" in text:
			checkValidDirection(tweet, "up")

		elif "down" in text:
			checkValidDirection(tweet, "down")

		else:
			notRecognised(tweet)


	addUser(finalMentions) # Add new users to the database

	a += 1