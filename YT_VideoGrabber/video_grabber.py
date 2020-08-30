import concurrent.futures
import json
import requests
import feedparser
import time


_LIMIT_VIDEOS = 3

def viewsConvert(views):
	_Billion = 1000000000
	_Million = 1000000
	_Thousand = 1000
	viewsInt = int(views)
	if(viewsInt//_Billion):
		return "{}B".format(str(round(viewsInt/_Billion,1)))
	elif(viewsInt//_Million):
		return "{}M".format(str(round(viewsInt/_Million,1)))
	elif(viewsInt//_Thousand):
		return "{}K".format(str(viewsInt//_Thousand))
	else:
		return views



def getV(impu):
	channelName=impu[0]
	feedUrl=impu[1]
	try:
		channelFeed = feedparser.parse(feedUrl)
	except:
		print('\n[!] Error Getting RSS Feed!, Are you conneced to Internet?\n')
		return {0}
	#print(channelName)
	grabbedDataChannelList = []
	grabbedDataChannelList.append(channelName)
	for ii in range(0,_LIMIT_VIDEOS):
		grabbedDataChannel = {}
		try:
			grabbedDataChannel['title'] = channelFeed['entries'][ii]['title']
			grabbedDataChannel['link'] = channelFeed['entries'][ii]['link']
			grabbedDataChannel['thumbnail'] = channelFeed['entries'][ii]['media_thumbnail'][0]['url']		
			grabbedDataChannel['views'] = viewsConvert(channelFeed['entries'][ii]['media_statistics']['views'])
		except Exception as e:
			print(e)
			print('\n[!] Error Getting RSS Feed DATA!, Are you added correct channel?\n')
			continue
		grabbedDataChannelList.append(grabbedDataChannel)
	return grabbedDataChannelList
	
	
def latestVideoGrab():
	try:
		cha = open('channels.json','r')	
		chaJson = json.load(cha)
		cha.close()
	except:
		print('[!] Error getting channels list!\n    Are the URLs added?, see help')
		exit(0)
	grabbedData = {}

	argum = [[channel, chaJson[channel]['feed']] for channel in chaJson]
	with concurrent.futures.ThreadPoolExecutor() as executor:
		futures = executor.map(getV, argum)

	saveF = {}
	for f in futures:
		saveF[f[0]] = f[1:]
	return saveF
