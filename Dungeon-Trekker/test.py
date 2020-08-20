from Connections.twitterAccess import *
from Connections.dbConnection import *

api = getAPI()

print(api.get_user('hjnewton_'))







	for x in mentions:
		counter = 0

		for y in dumpTweetList:
			counter += 1
			if str(x.id) == str(y):
				break
			elif counter == dumpListLength:
				finalList.append(x)
				executeUpdate("INSERT INTO Tweet_dump VALUES(" + str(x.id) + ");")
			else:
				pass
	
	return finalList