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
		urlEvent = 'https://graph.facebook.com/v2.2/'+id
		eventInfo = urlopen(urlEvent)		#in json format
		eventInfoDict = loads(eventInfo.read()) 	#in dictionary format
		if(debug):
			print eventInfoDict

			
		#second we get attendees list
		urlEventAttendees = 'https://graph.facebook.com/v2.2/'+id+'/attending?access_token=CAACEdEose0cBAEPtuZAZA5xHpmed019ZCGtx2KnnWquv4HusEIw7iFcjJUeGvOoZAjE2G0hZAvrXysrxKqOrFePEXSXTtArCPNkOlAeLVFDZBFUlWfOlEs1KNqZCzcUZCCEVeZCcD2tZB6QxPHsjHrqwgdZCdkKBlvJTGkYCbua6jCzGCYZCt9PRXTBYKOCAQ3mMPnHSq2mqkyK01ZAyPBXhgLfCr'
		#jsonData = urlopen('https://graph.facebook.com/v2.2/859809790727785/attending?access_token=CAACEdEose0cBAEPtuZAZA5xHpmed019ZCGtx2KnnWquv4HusEIw7iFcjJUeGvOoZAjE2G0hZAvrXysrxKqOrFePEXSXTtArCPNkOlAeLVFDZBFUlWfOlEs1KNqZCzcUZCCEVeZCcD2tZB6QxPHsjHrqwgdZCdkKBlvJTGkYCbua6jCzGCYZCt9PRXTBYKOCAQ3mMPnHSq2mqkyK01ZAyPBXhgLfCr')
		attendeeInfo = urlopen(urlEventAttendees)
		attendeeInfoDict = loads(attendeeInfo.read())
		if(debug):
			print attendeeInfoDict
		#content = loads(jsonData.read())
		#content = urlopen('https://graph.facebook.com/v2.2/859809790727785/attending?access_token=CAACEdEose0cBAEPtuZAZA5xHpmed019ZCGtx2KnnWquv4HusEIw7iFcjJUeGvOoZAjE2G0hZAvrXysrxKqOrFePEXSXTtArCPNkOlAeLVFDZBFUlWfOlEs1KNqZCzcUZCCEVeZCcD2tZB6QxPHsjHrqwgdZCdkKBlvJTGkYCbua6jCzGCYZCt9PRXTBYKOCAQ3mMPnHSq2mqkyK01ZAyPBXhgLfCr')
		#content = loads(urlopen('https://graph.facebook.com/v2.2/search?q=Rang Barsay&type=event').read())
		# print "type of data returned is :",type(content)
		# keyList = []
		# for key in content.keys():
		# 	print "key : %s" %(key)
		# 	keyList.append(key)
		# 	print "\n"
		# 	#print key, value
		# print content[keyList[1]][0]['id']
		#print keyList[1]['name']	
 		


fbapi1 = FBAPI_Events()
fbapi1.printMembers(859809790727785)