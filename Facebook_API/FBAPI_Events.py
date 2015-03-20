from urllib2 import urlopen
from simplejson import loads

'''
this class gets event data and also the list of people 
attending that event. 
Output is in dictionary format {key:value}
'''
debug = True
eventIdList = []
dataPerEvent = []
attendingCount = 0
declinedCount = 0
maybeCount = 0
access_token = 'CAACEdEose0cBAMFVm1c8Cy4JB9vmQPNb3joW3PFIA8zlJKPgxuhK8cblFeQ3WAKf9ZBV1KqI8tlZBBk7zyiMOZC7ZB1POUDJTB6ZAd4xNYsxGYWtTbTE6FmjPQb4sZBJIB1t4tZAa90zBD3yLPd6dZBVwJd5lTdDZBVyz6J4EagG6LsBSBOFeJn3LEsPLcYwM6ZCEonEsOLEtW31gtZAUc5pSUw'
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
		global access_token
		urlEvent = 'https://graph.facebook.com/v2.2/'+id+'?access_token='+access_token+'&limit=3000&offset=1'
		eventInfo = urlopen(urlEvent)		#in json format
		eventInfoDict = loads(eventInfo.read()) 	#in dictionary format
		if(debug):
			print eventInfoDict
		self.parseEventDetails(eventInfoDict)
		return eventInfoDict
		
		
	'''
	Function to call fb api and receive event invitees data - accept/decline/may be
	@param: id of the event
	'''	
	def getEventInvitees(self,urlEventInvitees):
		#second we get attendees list
		global access_token
		#urlEventInvitees = 'https://graph.facebook.com/v2.2/'+id+'/attending?access_token='+access_token
		inviteeInfo = urlopen(urlEventInvitees)
		inviteeInfoDict = loads(inviteeInfo.read())
		return inviteeInfoDict

	'''
	Function to parse event details in
	desired format
	@param: one event's info in dict format
	'''
	def parseEventDetails(self, eventInfoDict):
		global dataPerEvent
		dataPerEvent.append(eventInfoDict['name'])
		dataPerEvent.append(eventInfoDict['location'])
		dataPerEvent.append(eventInfoDict['start_time'])
		dataPerEvent.append(eventInfoDict['owner']['name'])
		dataPerEvent.append(eventInfoDict['owner']['id'])
		dataPerEvent.append(eventInfoDict['venue']['latitude'])
		dataPerEvent.append(eventInfoDict['venue']['longitude'])
		if debug:
			print dataPerEvent


	'''
	Function to parse event attendee info
	and count different categories
	@param: inviteeInfo in dictionary format
	'''
	def parseEventAttendee(self,id):
		global dataPerEvent, attendingCount, declinedCount, maybeCount			
		#Count attending users
		urlEventInvitees = 'https://graph.facebook.com/v2.2/'+id+'/attending?access_token='+access_token
		inviteeInfoDict = self.getEventInvitees(urlEventInvitees)
		while True: 
			attendingCount = attendingCount + len(inviteeInfoDict['data'])
			if  ('next' not in inviteeInfoDict['paging']):
				break
			inviteeInfoDict = self.getEventInvitees(inviteeInfoDict['paging']['next'])

		#Count declined users
		urlEventInvitees = 'https://graph.facebook.com/v2.2/'+id+'/declined?access_token='+access_token
		inviteeInfoDict = self.getEventInvitees(urlEventInvitees)
		while True:
			declinedCount = declinedCount + len(inviteeInfoDict['data'])
			if  ('next' not in inviteeInfoDict['paging']):
				break
			inviteeInfoDict = self.getEventInvitees(inviteeInfoDict['paging']['next'])

		#Count maybe users
		urlEventInvitees = 'https://graph.facebook.com/v2.2/'+id+'/maybe?access_token='+access_token
		inviteeInfoDict = self.getEventInvitees(urlEventInvitees)
		while True:
			maybeCount = maybeCount + len(inviteeInfoDict['data'])
			if  ('next' not in inviteeInfoDict['paging']):
				break
			inviteeInfoDict = self.getEventInvitees(inviteeInfoDict['paging']['next'])

		dataPerEvent.append(attendingCount)
		dataPerEvent.append(declinedCount)
		dataPerEvent.append(maybeCount)		
		# for key in inviteeInfoDict.keys():
		# 	print "Key found is : "+key
		# 	if(key == 'data'):
		# 		for i in range (0,len(inviteeInfoDict[key]),1):
		# 			print "inviteeInfoDict[key][i]['rsvp_status'] :"+ inviteeInfoDict[key][i]['rsvp_status']
		# 			print
		# 			if(inviteeInfoDict[key][i]['rsvp_status'] == 'attending'):
		# 				attendingCount=attendingCount + 1
		# 			elif(inviteeInfoDict[key][i]['rsvp_status'] == 'declined'):
		# 				declinedCount= declinedCount + 1
		# 			elif(inviteeInfoDict[key][i]['rsvp_status'] == 'unsure'):
		# 				maybeCount= maybeCount + 1			
		# 	elif(key == 'paging'): 
		# 		if('next' in inviteeInfoDict['paging']):
		# 			if(debug):
		# 				print "TRAVERSING TO THE NEXT PAGE!PLEASE WAIT...."
		# 			self.parseEventAttendee(self.getEventInvitees(inviteeInfoDict['paging']['next']))
		# 		else:
		# 			dataPerEvent.append(attendingCount)
		# 			dataPerEvent.append(declinedCount)
		# 			dataPerEvent.append(maybeCount)		
		# 			return


	'''
	This function will get its results from target search
	applied to graph api
	'''
	def getEventIdList(self):
		eventIdList.append('859809790727785')
			
	'''
	This function will get the events based on dates and 
	call other functions to fetch data from each event.
	'''
	def main(self):
		global eventIdList, dataPerEvent
		'Add code to do targetted search'
		self.getEventIdList()
		for i in range(0,len(eventIdList),1):
			eventInfoDict = self.getEventById(eventIdList[i])
			self.parseEventDetails(eventInfoDict)
			#urlEventInvitees = 'https://graph.facebook.com/v2.2/'+eventIdList[i]+'/invited?access_token='+access_token
			#inviteeInfoDict = self.getEventInvitees(eventIdList[i])
			self.parseEventAttendee(eventIdList[i])
			print dataPerEvent
			dataPerEvent = []
			maybeCount = 0
			attendingCount = 0
			declinedCount = 0


eventObj = FBAPI_Events()
eventObj.main()
# eventObj.getEventIdList()
# eventObj.getEventById(eventIdList[0])


 		



