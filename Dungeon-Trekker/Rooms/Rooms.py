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

def room12(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You are now the depths of the dungeon. You can hear a dripping noise as you walk down the stairs. As you take your last step you fall into water. The water is freezing, you need to act quick.\n\nSwim forward\nSwim left\nSwim right", tweet.id)

def room13(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You go around the corner to see if you can find anything that could give you a hint as to where the Althaz treasure is. As you look around you spot a hole in the ceiling of the corridor.\n\nClimb up\nTrek forward", tweet.id)

def room14(tweet):
	api.update_status("@" + tweet.user.screen_name + " It's a dead end! You decide to walk back to the entrance of the dungeon to see if you can find anything that will make it easier to see.\n\nWalk back", tweet.id)

def room15(tweet):
 	api.update_status("@" + tweet.user.screen_name + " The water is freezing and you know you can't stay in for much longer. You see a crack in the wall which could help you get out of the water.\n\nClimb up\nKeep swimming forward", tweet.id)

def room16(tweet):
 	api.update_status("@" + tweet.user.screen_name + " The water is freezing and you know you can't stay in for much longer. You keep swimming forward and spot a light emerging around the corner, you decide to follow it.\n\nGo left", tweet.id)

def room17(tweet):
 	api.update_status("@" + tweet.user.screen_name + " The water is freezing and you know you can't stay in for much longer. It is very dark so you are only going off your sense of touch. You feel a way to the left and a way to the right, where will you go?\n\nCheck right\nCheck left", tweet.id)

def room18(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You climb up into the crevice and begin to crawl through the narrow cave. It is very dark so you are only going off your sense of touch. You feel a way to the left and a way to the right, where will you go?\n\nCrawl left\nCrawl right", tweet.id)

def room19(tweet):
 	api.update_status("@" + tweet.user.screen_name + " There are some stairs going up to a pitch black room, you are starting to feel like you are being watched so you have to be careful.\n\nSneak up", tweet.id)

def room20(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You climb up onto the wall and you spot an opening above you. You keep climbing and get to a secret passage way. You begin to crawl through the passage when you see what looks like a ramp. You decide to slide down.\n\nSlide down", tweet.id)

def room21(tweet):
 	api.update_status("@" + tweet.user.screen_name + " It's now pitch black and you do not know which way you came from. You need to get out of the water NOW or you will die. You take a risk and dive underwater to find something that might help you.\n\nSwim down", tweet.id)

def room22(tweet):
 	api.update_status("@" + tweet.user.screen_name + " As you turn the corner everything starts to rumble and you hear a screech. You look around and need to make a decision fast.\n\nRight passage\nLeft passage", tweet.id)

def room23(tweet):
 	api.update_status("@" + tweet.user.screen_name + " Finally, there seems to be a staircase coming out of the water. You crawl up the staircase, shaking from the cold of the water. You notice that there are some doors at the end of the corridor.\n\nDoor down\nDoor forward\nDoor right\nDoor left", tweet.id)

def room24(tweet):
 	api.update_status("@" + tweet.user.screen_name + " As you turn the corner you hear a loud bang. Everything starts to rumble. You look around and need to make a decision fast.\n\nRight corridor\nLeft corridor\nStairs up", tweet.id)

def room25(tweet):
 	api.update_status("@" + tweet.user.screen_name + " The passage ahead is blocked by rocks, you decide to go back to the passage on the ceiling\n\nBack", tweet.id)

def room26(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You make it to the bottom. You can feel a loose rock on the wall and you pull it off. As you do the water starts to drain from the corridors. When the water has gone you can see two doors, which one will you choose?\n\nOpen right\nOpen left", tweet.id)

def room27(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You end up in a huge room with shrines everywhere, you look around the room and spot a big wooden door on top of a grand staircase. What could it be?\n\nWalk up", tweet.id)

def room28(tweet):
 	api.update_status("@" + tweet.user.screen_name + " As you approach the door you see some text written above: 'I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?'\n\nHINT: To respond to a riddle, just type the answer.", tweet.id)

def room29(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You have made it past the door, go you! You feel like you must be reaching the end of your journey, you have been traveling for days. As the lights come on you look down and see that the room is a huge pit with ledges to jump on.\n\nHop down", tweet.id)

def room30(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You have jumped down onto the first ledge. You pull a torch off the wall and throw it off into the pit. It seems to go on forever until there is a splash and the torch goes out. Do you risk jumping off or work your way down?\n\nJump down\nJump right", tweet.id)

def room31(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You decide to take the risk and jump down into the water. 1...2...3...GO! You land into the water below but it isn't what you expected. You land in goo, it's thick and disgusting.\n\nWade forward\nWade left", tweet.id)

def room32(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You decide to take it slowly and go down the ledges, good choice. You jump to a ledge on the right and grab onto the wall. As you look around you notice a few places you could go.\n\nJump forward\nJump left", tweet.id)

def room33(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You struggle through the sticky goo and start to get tired, you cannot keep going through this liquid or you will get stuck. Do you sprint to get out of it quick, or take it slow and try and save your energy?\n\nSprint forward\nWalk right", tweet.id)

def room34(tweet):
 	api.update_status("@" + tweet.user.screen_name + " The goo starts to thin, thank god. You start to hear a rumble behind you and turn around to see what it could be when all of a sudden, a cluster of giant spiders sprint towards you. Think fast!\n\nSprint forward\nHide left", tweet.id)

def room35(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You jump left onto a ledge and only just make it. As you scramble on the edge you slip and fall onto the ledge below. There is a door to your left and a ledge blow you,\n\nLeap down\nGo left", tweet.id)

def room36(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You land onto a ledge on the right and scope out the next move you can make. You decide that you will have to make a leap of faith, but where to?\n\nLeap down\nLeap left", tweet.id)

def room37(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You walk right and end up finding a passage you can go down, the passage seems to lead to a dark, empty room.\n\nAmble forward", tweet.id)

def room38(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You decide to hide. You jump into the goo so it is covering you and hold your breath. You hear the stomping of their legs running past you, then...quiet. You leave it 10 minutes and then emerge taking a deep breathe.\n\nAmble forward", tweet.id)

def room39(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You land on the edge of the ledge. Scrambling to try and stay on you slip and fall into a pool of water below. You're a little dazed, as you sit up you see two doors.\n\nEnter left\nEnter right", tweet.id)

def room40(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You land on the edge of a platform. Scrambling to try and stay on you slip and fall into a pool of water below. You're a little dazed, as you sit up you see two doors.\n\nEnter left\nEnter right", tweet.id)

def room41(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You enter a room which has candles all over it. It is too bright to see anything properly. You squint and try to look for a way to go. You spot a staircase, which way will it be?\n\nDown stairs\nUp stairs", tweet.id)

def room42(tweet):
 	api.update_status("@" + tweet.user.screen_name + " You enter a pitch black room, it smells awful. All of a sudden you hear a Squelch. The lights ignite, you realise you are in a room filled with what seems to be rotting flesh! You put your shirt over your mouth and carry on.\n\nDown stairs\nUp stairs", tweet.id)

def room90(tweet):
	api.update_status("@" + tweet.user.screen_name + " You have done it, You're in the dungeon! This is where the real challenge begins. It is pitch black, do you search for a light or keep going?\n\nSearch", tweet.id)

def room91(tweet):
	api.update_status("@" + tweet.user.screen_name + " You go around the corner to see if you can find anything that could give you a hint as to where the Althaz treasure is. As you look around you spot a hole in the ceiling of the corridor.\n\nClimb up", tweet.id)


def room(tweet):
 	api.update_status("@" + tweet.user.screen_name + " ", tweet.id)
