from Connections.twitterAccess import *
from Connections.dbConnection import *
from DatabaseFunctions.DBFunctions import *

import tweepy
import time

api = getAPI()
currentMentions = None # List of the current tweet mentions
finalMentions = None # List of tweets that havent been replied to
a = 0
users = []

while(a < 1):
	currentMentions = api.mentions_timeline() # Get mentions in a list variable

	finalMentions = updateMentions(currentMentions) # Return a list of tweets in the mentions that havent had a reply

	addUser(finalMentions)

	refreshDBTweets()



	a += 1