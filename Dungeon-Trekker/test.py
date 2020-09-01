from Connections.twitterAccess import *
#from Connections.dbConnection import *

api = getAPI()

while(True):
	tweets = api.user_timeline()
	for x in tweets:
		api.destroy_status(x.id)