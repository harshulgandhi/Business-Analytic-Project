from urllib2 import urlopen
from simplejson import loads
from FBAPI_Events import FBAPI_Events
'''
This class calls FBAPI_Event class to get 
event attendees list. 
It fetches the friends of the attendees
and checks if these friends are also attending
the same event
'''
debug = True
class FBAPI_AttendeeFriends:
	'Class to make API calls to facebook and fetch friends of users'
	def __init__(self,eventId):
		print "Fetching list of friends for attendees...."
		# fbapi1 = FBAPI_Events()
		# attendeeInfoDict = fbapi1.getEventById(eventId)
		# fl = open('attending.txt',"w")
		# print type(attendeeInfoDict)
		# fl.write(str(attendeeInfoDict))
		# if(debug):
		# 	#print attendeeInfoDict
		# 	print "Printing ID of first attendee"
		# 	keyList = []
		# 	for key in attendeeInfoDict.keys():
		# 		keyList.append(key)
			# for i in range (0,len(attendeeInfoDict[keyList[1]]),1):
			#  	if(attendeeInfoDict[keyList[1]][i]['name'] == 'Shakiya Sha'):
			#  		print attendeeInfoDict[keyList[1]][i]['id']
			#  		break

	def getFriendsList(self,id):
		accessToken = 'CAACEdEose0cBAGaZAJdSfmJDbMzWBmZCrHD44yGdFuxocRRxfGYn3mL7quttIA0Ir419uxUnm6SfPlU9sYl39aXl2DRmtCJFaQF3rpipBL5N4VRhIyrnPrtHV7my6KgRjhsFvP3iCZAWvvnmrjXh5Hs3nY13byCY7wTAl7MAKFyp05h7YZCqShIgl289rMoH7cs63Wc0KpmDpdHKx2wP'
		urlGetFriends = 'https://graph.facebook.com/v1.0/'+id+'/friends?access_token='+accessToken 		#+'/friends?access_token='+accessToken
		if(debug):
			print 'urlGetFriends : '+urlGetFriends
		#url = 'https://graph.facebook.com/v2.2/1094488052/friends?limit=25&offset=25&__after_id=enc_AdBofZBoJg1Tj0jeztIFtgOsHuJhXpEOZCquLKPeAhee1GBZAOwGeKzzOoNzFKfDntcUcTdBgABhX8HvXBrEzacBDaO'
		friendsList = urlopen(urlGetFriends)
		friendsListDict = loads(friendsList.read())

		print "######################"
		print friendsListDict


	'''
	Function to check connection between two ids
	@param id1: id of first user
	@param id2: id of second user
	'''
	def checkConnection(self,id1,id2):
		accessToken = 'CAACEdEose0cBAGaZAJdSfmJDbMzWBmZCrHD44yGdFuxocRRxfGYn3mL7quttIA0Ir419uxUnm6SfPlU9sYl39aXl2DRmtCJFaQF3rpipBL5N4VRhIyrnPrtHV7my6KgRjhsFvP3iCZAWvvnmrjXh5Hs3nY13byCY7wTAl7MAKFyp05h7YZCqShIgl289rMoH7cs63Wc0KpmDpdHKx2wP'
		urlGetConnection = 'https://graph.facebook.com/v2.2/'+id1+'/friends/'+id2+'?access_token='+accessToken
		status = urlopen(urlGetConnection)
		if(status is null):
			return False
		else:
			return True



	'''
	Function to check connection between two attendees of a particular event
	@param: eventID
	'''
	def checkAttendeesConnection(self,eventId):
		print "Fetching list of friends for attendees...."
		fbapi1 = FBAPI_Events()
		attendeeInfoDict = fbapi1.getEventById(eventId)
		fl = open('attending.txt',"w")
		print type(attendeeInfoDict)
		fl.write(str(attendeeInfoDict))
		for key0 in attendeeInfoDict.keys():
			for i in range(0,len(attendeeInfoDict[key0]),1):
				for j in range (i,len(attendeeInfoDict[key0]),1):
					areConnected = checkConnection(attendeeInfoDict[key0][i]['id'],attendeeInfoDict[key0][j]['id'])
					if(areConnected):
						print attendeeInfoDict[key0][i]['name']+" is connected to "+attendeeInfoDict[key0][j]['name']




eventId = '859809790727785'
fbapi_friends = FBAPI_AttendeeFriends(eventId)
fbapi_friends.checkAttendeesConnection(eventId)
#fbapi_friends.getFriendsList('10203052496012771')