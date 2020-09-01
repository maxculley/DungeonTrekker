from Connections.twitterAccess import *

import tweepy

api = getAPI()



def room1(tweet):
	api.update_status("@" + tweet.user.screen_name + " You are the famous treasure hunter 'Trekker " + tweet.user.name + "'. You are in the forest looking for the entrance to the dungeons where the mythical Althaz riches are. Your options are:\n\nForward", tweet.id)

def room2(tweet):
	api.update_status("@" + tweet.user.screen_name + " You walk further into the forest for what seems like an eternity. You see a bag proped up against a tree and decide to take it, you can store codes inside your bag.\n\nYour options are:\n\nContinue forward", tweet.id)

def room3(tweet):
	api.update_status("@" + tweet.user.screen_name + " You are in the depths of the forest, no going back now. You start to hear a noise, unsure what is it you start to walk more stealthily. The path ahead forks into two, where will you go?\n\nSneak Left\nSneak Right", tweet.id)

def room4(tweet):
	api.update_status("@" + tweet.user.screen_name + " You sneak left towards what looks like a swamp, you hear the buzz of the bugs flying around your head. The swamp is sure to give you a disease, best not go in it. As you turn around you see a piece of paper in a tree, what is it?\n\nRight", tweet.id)

def room5(tweet):
	api.update_status("@" + tweet.user.screen_name + " You decided to sneak down the right passage, as you crawl through the leaves of the plants surrounding you, you see a piece of paper flapping in the distance, what could it be?\n\nLeft", tweet.id)

def room6(tweet):
	api.update_status("@" + tweet.user.screen_name + " You walk towards the piece of paper and as you get closer you realise what it is, it's a code!\n\nAdded x1 code *H-Y-M-E-R*\nHINT: Codes have letters which can be rearranged to create words.\n\nWalk forward", tweet.id)

def room7(tweet):
	api.update_status("@" + tweet.user.screen_name + " You have been walking for hours with no sign of the entrance and you are starting to lose hope. You take a seat on a nearby rock to have a drink, when all of a sudden there is a click. You jump up and a passage appears beneath you.\n\nDown", tweet.id)

def room8(tweet):
	api.update_status("@" + tweet.user.screen_name + " You have made it to the entrance of the dungeon, however there seems to be a stone passcode needed to enter. If only you had a code...\n\nHINT: To enter a code just type what you think the code is and send the tweet!", tweet.id)

def room9(tweet):
	api.update_status("@" + tweet.user.screen_name + " You have done it, You're in the dungeon! This is where the real challenge begins. It is pitch black, do you search for a light or keep going?\n\nSearch\nGo forward", tweet.id)

def room10(tweet):
	api.update_status("@" + tweet.user.screen_name + " You search around on the floor. You feel something that feels like a lever. You pull it, all of a sudden torches on the walls ignite. You see a passage to the right and a flight of stairs going down, where do you go?\n\nGo right\nGo down", tweet.id)

def room11(tweet):
	api.update_status("@" + tweet.user.screen_name + " It is still pitch black, at this rate you'll end up getting lost. It is starting to feel a lot colder and get a lot more eerie.\n\nSneak forward\nGo back", tweet.id)

def room14(tweet):
	api.update_status("@" + tweet.user.screen_name + " It's a dead end! You decide to walk back to the entrance of the dungeon to see if you can find anything that will make it easier to see.\n\nWalk back", tweet.id)

def room90(tweet):
	api.update_status("@" + tweet.user.screen_name + " You have done it, You're in the dungeon! This is where the real challenge begins. It is pitch black, do you search for a light or keep going?\n\nSearch", tweet.id)




# def room5(tweet):
# 	api.update_status("@" + tweet.user.screen_name + " ", tweet.id)