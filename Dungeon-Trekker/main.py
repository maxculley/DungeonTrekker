from Connections.twitterAccess import *
from Connections.dbConnection import *

import tweepy
import time

api = getAPI()
currentMentions = None
a = 0

while(a < 1):
	# time.sleep(12)
	currentMentions = api.mentions_timeline()
	for x in currentMentions:
		print(x.text)
		print(x.id)

	a += 1