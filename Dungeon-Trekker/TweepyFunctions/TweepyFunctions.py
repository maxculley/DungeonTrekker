from Connections.twitterAccess import *
from DatabaseFunctions.DBFunctions import *

import tweepy

api = getAPI()

def start(tweet):
	return checkUserGame(tweet.user.id)

def resume(tweet):
	api.update_status("@" + tweet.user.screen_name + " If you would like to resume your current game, please type 'resume'.\nIf you would like to start a new game, please type 'new'.", tweet.id)

def new(tweet):
	api.update_status("@" + tweet.user.screen_name + " You have started a new game!", tweet.id)

def resumeGame(tweet):
	if checkUserGame(tweet.user.id) == True:
		api.update_status("@" + tweet.user.screen_name + " You have resumed your current game!", tweet.id)
	else:
		api.update_status("@" + tweet.user.screen_name + " You have no game to resume, so you have started a new game!", tweet.id)

def commands(tweet):
	api.update_status("@" + tweet.user.screen_name + " These are the commands:\n\nStart - Start game\nNew - New game\nResume - Resume game\nCommands - Check commands\nHelp - Get help from the team", tweet.id)

def help(tweet):
	api.send_direct_message(tweet.user.id, "Hi! We noticed you needed some help, how can we assist you?")

def notRecognised(tweet):
	api.update_status("@" + tweet.user.screen_name + " This command was not recognised, to see a list of possible commands please type 'commands'.", tweet.id)