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

	refreshDBTweets() # Clean database
	finalMentions = getFinalMentions() # Get all final tweets

	for tweet in finalMentions:
		text = (tweet.text).lower() # Turn the tweet text lowercase
		text = text.split(" ", 1)[1] # Get the content of the tweet

		print("Tweet text: " + text)

		if text == "start":
			result = start(tweet)

			if result == True:
				resume(tweet)
			else:
				new(tweet)
		elif text == "resume":
			resumeGame(tweet)
		elif text == "new":
			new(tweet)
		elif text == "commands":
			commands(tweet)
		elif text == "help":
			help(tweet)
		else:
			notRecognised(tweet)


	addUser(finalMentions) # Add new users to the database

	a += 1