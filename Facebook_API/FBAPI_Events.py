from urllib2 import urlopen
from simplejson import loads

'''
this class gets event data and also the list of people 
attending that event. 
It creates a list of event and there corresponding attendees.
'''
debug = True
class FBAPI_Events:
	'Class to make API calls to facebook and fetch event details'
	def __init__(self):
		print "Fetching events data, please wait..."

	'''
	Function to call fb api and receive events data - including list of attendees
	@param: id of the event
	'''
	def getEventById(self, id):
		#first we get event info only
		urlEvent = 'https://graph.facebook.com/v2.2/'+id+'/?access_token=CAACEdEose0cBAAqnNgZCcioLpbvaCqAW2yaWiwJRWr18b3PAvCXmTU0t4HvuqwZCmzZAZCzZBRdfvvVo8uEFF5TOmqjBsI3qCiQ0KcnaSRybRS9CKjuHKJmwpVZAnOg9xi7mMoPgru6inTi7ZAz6sZABjXhWTzGKDKtNcJCsOBDfnSc7ZAHT5StgqDeW44ZAfRTCEeUlvHHZAxEJloCt2vKRgxq'
		eventInfo = urlopen(urlEvent)		#in json format
		eventInfoDict = loads(eventInfo.read()) 	#in dictionary format
		if(debug):
			print eventInfoDict

			
		#second we get attendees list
		urlEventAttendees = 'https://graph.facebook.com/v2.2/'+id+'/attending?access_token=CAACEdEose0cBAAqnNgZCcioLpbvaCqAW2yaWiwJRWr18b3PAvCXmTU0t4HvuqwZCmzZAZCzZBRdfvvVo8uEFF5TOmqjBsI3qCiQ0KcnaSRybRS9CKjuHKJmwpVZAnOg9xi7mMoPgru6inTi7ZAz6sZABjXhWTzGKDKtNcJCsOBDfnSc7ZAHT5StgqDeW44ZAfRTCEeUlvHHZAxEJloCt2vKRgxq'
		#jsonData = urlopen('https://graph.facebook.com/v2.2/859809790727785/attending?access_token=CAACEdEose0cBAEPtuZAZA5xHpmed019ZCGtx2KnnWquv4HusEIw7iFcjJUeGvOoZAjE2G0hZAvrXysrxKqOrFePEXSXTtArCPNkOlAeLVFDZBFUlWfOlEs1KNqZCzcUZCCEVeZCcD2tZB6QxPHsjHrqwgdZCdkKBlvJTGkYCbua6jCzGCYZCt9PRXTBYKOCAQ3mMPnHSq2mqkyK01ZAyPBXhgLfCr')
		attendeeInfo = urlopen(urlEventAttendees)
		attendeeInfoDict = loads(attendeeInfo.read())
		if(debug):
			print attendeeInfoDict
			print "Printing ID of first attendee"
			keyList = []
			for key in attendeeInfoDict.keys():
				keyList.append(key)
			print attendeeInfoDict[keyList[1]][0]['id']
			
			
		#content = loads(urlopen('https://graph.facebook.com/v2.2/search?q=Rang Barsay&type=event').read())
		
		# keyList = []
		# for key in content.keys():
		# 	print "key : %s" %(key)
		# 	keyList.append(key)
		# 	print "\n"
		
		# print content[keyList[1]][0]['id']
		
 		


fbapi1 = FBAPI_Events()
fbapi1.getEventById('859809790727785')


