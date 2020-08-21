from Connections.twitterAccess import *

import tweepy

api = getAPI()


def commands(tweet):
	api.update_status("@" + tweet.user.screen_name + " These are the commands:", tweet.id)

def notRecognised(tweet):
	api.update_status("@" + tweet.user.screen_name + " This command was not recognised, to see a list of possible commands please type 'commands'.", tweet.id)