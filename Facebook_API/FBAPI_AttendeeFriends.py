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
	def __init__(self):
		print "Fetching list of friends for attendees...."
		fbapi1 = FBAPI_Events()
		attendeeInfoDict = fbapi1.getEventById('859809790727785')
		if(debug):
			#print attendeeInfoDict
			print "Printing ID of first attendee"
			keyList = []
			for key in attendeeInfoDict.keys():
				keyList.append(key)
			# for i in range (0,len(attendeeInfoDict[keyList[1]]),1):
			# 	if(attendeeInfoDict[keyList[1]][i]['name'] == 'Shakiya Sha'):
			# 		print attendeeInfoDict[keyList[1]][i]
			# 		break

	def getFriendsList(self,id):
		accessToken = 'CAACEdEose0cBAG0nIoxCXAwko1p0RHarL7exWjACFcNBgCIVLZCfVeyC4YLqj0yBXYZBjL3FoFpcG4lRe7XkxFSfjsWCnMBGdqKfGNKVijKRSZCYyXNp7oh8455kWIN5DPRXNpP62idOePwefWFkhZAfB9TDAyjXnjc2Pad0TztQZCxCFpMZBD3LmMbE5i3Gmb6qIdWGUcQYZAML6SfHIpJ'
		urlGetFriends = 'https://graph.facebook.com/v2.2/'+id+'/friends?access_token='+accessToken 		#+'/friends?access_token='+accessToken
		if(debug):
			print 'urlGetFriends : '+urlGetFriends
		#url = 'https://graph.facebook.com/v2.2/1094488052/friends?limit=25&offset=25&__after_id=enc_AdBofZBoJg1Tj0jeztIFtgOsHuJhXpEOZCquLKPeAhee1GBZAOwGeKzzOoNzFKfDntcUcTdBgABhX8HvXBrEzacBDaO'
		friendsList = urlopen(urlGetFriends)
		friendsListDict = loads(friendsList.read())

		print "######################"
		print friendsListDict['data'][4]



fbapi_friends = FBAPI_AttendeeFriends()
fbapi_friends.getFriendsList('1094488052')