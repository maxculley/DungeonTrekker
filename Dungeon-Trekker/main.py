from Connections.twitterAccess import *
from Connections.dbConnection import *
from DatabaseFunctions.DBFunctions import *

import tweepy
import time

api = getAPI()
currentMentions = None # List of the current tweet mentions
updatedMentions = []
currentID = None # CurrentID of tweet working on
a = 0
found = False


while(a < 1):
	currentMentions = api.mentions_timeline() # Get mentions in a list variable

	updatedMentions = checkMentions(currentMentions) # Check if mentions have already been replied to
	print(updatedMentions)

	for x in updatedMentions:
		currentID = x

		print("Updated Tweet")
		executeUpdate("UPDATE General SET latest_mention_id = '" + str(currentID) + "'")
	a += 1