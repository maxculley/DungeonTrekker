from Connections.twitterAccess import *
from Connections.dbConnection import *
from DatabaseFunctions.DBFunctions import *

import tweepy
import time

api = getAPI()
cursor = getCursor()
currentMentions = None
a = 0
currentID = None

while(a < 1):
	# time.sleep(12)
	currentMentions = api.mentions_timeline()
	for x in currentMentions:
		currentID = x.id
	print(currentID)
	executeQuery("UPDATE General SET latest_mention_id = '" + str(currentID) + "'")
	a += 1