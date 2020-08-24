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
		text = (tweet.text).lower()
		text = text.split(" ", 1)[1]
		print("Tweet text: " + text)

		if text == "commands":
			commands(tweet)
		else:
			notRecognised(tweet)


	addUser(finalMentions)




	a += 1