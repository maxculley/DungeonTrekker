from Connections.twitterAccess import *
from DatabaseFunctions.DBFunctions import *

import tweepy

api = getAPI()



def getCurrentMentions():
	return api.mentions_timeline() # Return all mentions in a list variable


def getFinalMentions():
	currentMentions = getCurrentMentions()
	return updateMentions(currentMentions) # Return a list of tweets in the mentions that haven't had a reply