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
			print attendeeInfoDict
			print "Printing ID of first attendee"
			keyList = []
			for key in attendeeInfoDict.keys():
				keyList.append(key)
			print attendeeInfoDict[keyList[1]][0]['id']




fbapi_friends = FBAPI_AttendeeFriends()