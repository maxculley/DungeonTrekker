from Connections.twitterAccess import *

import tweepy

api = getAPI()



def room1(tweet):
	api.update_status("@" + tweet.user.screen_name + " You are the famous treasure hunter " + tweet.user.name + ". You are in the forest looking for the entrance to the dungeons where the mythical Althaz riches are. Your options are:\n\nForward", tweet.id)

def room2(tweet):
	api.update_status("@" + tweet.user.screen_name + " You walk further into the forest for what seems like an eternity. You see a bag proped up against a tree and decide to take it.\n\nGained +1 bag (+2 Storage)\nHINT: To see your stats just type 'stats'\n\nYour options are:\n\nContinue forward", tweet.id)

def room3(tweet):
	api.update_status("@" + tweet.user.screen_name + " You are in the depths of the forest, no going back now. You start to hear a noise, unsure what is it you start to walk more stealthily. The path ahead forks into two, where will you go?\n\nSneak Left\nSneak Right", tweet.id)