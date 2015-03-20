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
	accessToken = 'CAACEdEose0cBAMx8ChDs83qfXaAjBJBFRn1cZCNxeQJUiA6K5KGID45yuindTZAtwZBdIYKvrVP6PlUzMIT61OfI2204PCUoAni9Ssav6YVqcx17ciUHUj2bGkpd9cnTilCfutRp4RNbpBaQfflYXljZBPqALpbtSP6HedDZC1ZBWKwsWYzZBAK0RoC5KSYpVKdsZCXpgy9XFtCGZBmcXXTfY' 
	def __init__(self,eventId):
		print "Fetching list of friends for attendees...."
		fbapi1 = FBAPI_Events()
		attendeeInfoDict = fbapi1.getEventById(eventId)
		fl = open('attending.txt',"w")
		#print type(attendeeInfoDict)
		fl.write(str(attendeeInfoDict))
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
		#global accessToken
		urlGetFriends = 'https://graph.facebook.com/v1.0/'+id+'/friends?access_token='+self.accessToken  		#+'/friends?access_token='+accessToken
		if(debug):
			print 'urlGetFriends : '+urlGetFriends
		#url = 'https://graph.facebook.com/v2.2/1094488052/friends?limit=25&offset=25&__after_id=enc_AdBofZBoJg1Tj0jeztIFtgOsHuJhXpEOZCquLKPeAhee1GBZAOwGeKzzOoNzFKfDntcUcTdBgABhX8HvXBrEzacBDaO'
		friendsList = urlopen(urlGetFriends)
		friendsListDict = loads(friendsList.read())
		if(debug):
			print "######################"
			print friendsListDict


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
		for key in attendeeInfoDict.keys():

			if debug:
				test = open('testresult.txt',"w")
				if(key == "data"):
					print "\nNumber of attending users retrieved is : "+str(len(attendeeInfoDict[key]))+"\n"
					for i in range(1,len(attendeeInfoDict[key]),1):
						for j in range (i,len(attendeeInfoDict[key]),1):
							if(debug):
								print "To debug"
								print "ids being checked are "+attendeeInfoDict[key][i]['id']+" AND "+attendeeInfoDict[key][j]['id']
							areConnected = self.checkConnection(attendeeInfoDict[key][i]['id'],attendeeInfoDict[key][j]['id'])
							if areConnected:
								print attendeeInfoDict[key][i]['name'].decode('utf-8')+" is connected to "+attendeeInfoDict[key][j]['name'].decode('utf-8')
								return
							# elif areConnected==False:
							#  	print str(attendeeInfoDict[key][i]['name'].decode('utf-8'))+" is **NOT** connected to "+str(attendeeInfoDict[key][j]['name'].decode('utf-8'))



	'''
	Function to check connection between two ids
	@param id1: id of first user
	@param id2: id of second user
	'''
	def checkConnection(self,id1,id2):
		global accessToken
		urlGetConnection = 'https://graph.facebook.com/v2.2/'+id1+'/friends/'+id2+'?access_token='+self.accessToken
		status = loads(urlopen(urlGetConnection).read())
		if(debug):
			print "status returned is "+str(status['data'])
		if(len(status['data']) == 0):
			if(debug):
				print "Returning false"
			return False
		else:
			return True




eventId = '859809790727785'
fbapi_friends = FBAPI_AttendeeFriends(eventId)
fbapi_friends.checkAttendeesConnection(eventId)
#fbapi_friends.getFriendsList('10203052496012771')