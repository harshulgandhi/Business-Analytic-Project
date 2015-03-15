from urllib2 import urlopen
from simplejson import loads

'''
this class gets event data and also the list of people 
attending that event. 
Output is in dictionary format {key:value}
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
		access_token = 'CAACEdEose0cBAIS2Yfvx57EPnwVpZCKPSdCRNCe0gp2r8B3USbYgsctdWHYQXZBHZAyUMC43FEnPDBtOdeG6B9pvstTNTLRligtCN7d42FlLZABdYgjZAEn6YInVwBseVLh6dgwjAj5oknJWkrvuzX9muBSNNfLX1St2Wo08vpRnTUyTExjfYkCvtSLV0UbPSoZANl6O0OMIVaFO7ihbZB3'
		urlEvent = 'https://graph.facebook.com/v2.2/'+id+'/?access_token='+access_token
		eventInfo = urlopen(urlEvent)		#in json format
		eventInfoDict = loads(eventInfo.read()) 	#in dictionary format
		if(debug):
			print eventInfoDict

			
		#second we get attendees list
		urlEventAttendees = 'https://graph.facebook.com/v2.2/'+id+'/attending?access_token='+access_token
		#jsonData = urlopen('https://graph.facebook.com/v2.2/859809790727785/attending?access_token=CAACEdEose0cBAEPtuZAZA5xHpmed019ZCGtx2KnnWquv4HusEIw7iFcjJUeGvOoZAjE2G0hZAvrXysrxKqOrFePEXSXTtArCPNkOlAeLVFDZBFUlWfOlEs1KNqZCzcUZCCEVeZCcD2tZB6QxPHsjHrqwgdZCdkKBlvJTGkYCbua6jCzGCYZCt9PRXTBYKOCAQ3mMPnHSq2mqkyK01ZAyPBXhgLfCr')
		attendeeInfo = urlopen(urlEventAttendees)
		attendeeInfoDict = loads(attendeeInfo.read())
		return attendeeInfoDict

			
		#content = loads(urlopen('https://graph.facebook.com/v2.2/search?q=Rang Barsay&type=event').read())
		
		# keyList = []
		# for key in content.keys():
		# 	print "key : %s" %(key)
		# 	keyList.append(key)
		# 	print "\n"
		
		# print content[keyList[1]][0]['id']
		
 		



