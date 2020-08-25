from Connections.twitterAccess import *

import tweepy

api = getAPI()



def room1(tweet):
	api.update_status("@" + tweet.user.screen_name + " You are the famous treasure hunter " + tweet.user.name + ". You are in the forest looking for the entrance to the dungeons where the mythical Althaz riches are. Your options are:\n\nForward", tweet.id)