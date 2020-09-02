from Connections.twitterAccess import *

import tweepy

api = getAPI()

def favourite(tweet):
	api.create_favorite(tweet.id)

def resume(tweet):
	api.update_status("@" + tweet.user.screen_name + " If you would like to resume your current game, please type 'resume'.\nIf you would like to start a new game, please type 'new'.", tweet.id)

def resumeGame(tweet, hasGame):
	if hasGame == True:
		api.update_status("@" + tweet.user.screen_name + " You have resumed your current game!", tweet.id)
	else:
		api.update_status("@" + tweet.user.screen_name + " You have no game to resume, so you have started a new game!", tweet.id)

def commands(tweet):
	api.update_status("@" + tweet.user.screen_name + " These are the commands:\n\nStart - Start game\nNew - New game\nResume - Resume game\nCommands - Check commands\nHelp - Get help from the team", tweet.id)

def help(tweet):
	api.send_direct_message(tweet.user.id, "Hi! We noticed you needed some help, how can we assist you?")

def stats(tweet, users):
	api.send_direct_message(tweet.user.id, "Stats:\n\nUsers: " + str(users) + "")

def howToPlay(tweet):
	api.send_direct_message(tweet.user.id, "Hi " + tweet.user.name + ", welcome to Dungeon Trekker, your adventure starts here!\n\nThis is just a quick message showing you how to play the game. You will recieve tweets as you progress through the game telling you what kind of room you're in and what your moving options are. A tweet will look like this:\n\n\nYou are in a room, it has 4 walls and a roof with doors on two walls, what do you do?\n\nJump forward\nMove back\n\n\nHere you can see that there is some text about the room and then some options below. It is very important that when you type your option you type out what is shown, for instance if you want to move forward you would type 'Jump forward' NOT 'forward'. This is just so twitter doesn't tell you your tweets are duplicates.\n\nAnyway that's it from us! If you need help or any additional information, just tweet us 'help' or send us a direct message and you'll be able to speak to a real person who can solve your issue.\n\nThanks for playing! Happy trekking!")

def directionNotRecognised(tweet):
	api.update_status("@" + tweet.user.screen_name + " That direction is invalid! Please enter a valid way to go to proceed.", tweet.id)

def incorrectCode(tweet):
	api.update_status("@" + tweet.user.screen_name + " That code is incorrect, try again!", tweet.id)

def incorrectRiddle(tweet):
	api.update_status("@" + tweet.user.screen_name + " That answer is incorrect, try again!", tweet.id)

def notRecognised(tweet):
	api.update_status("@" + tweet.user.screen_name + " This command was not recognised, to see a list of possible commands please type 'commands'.", tweet.id)

def gameIsDown():
	api.send_direct_message(759343803723608064, "The game is down")