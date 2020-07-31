import feedparser
import json
import requests
import os
import time
import re
import argparse
import sys
from shutil import copyfile

channelRssLink = 'https://invidio.us/feed/channel/'
channelLink = 'https://invidio.us/channel/'



def newUrlAdd(newLink):
	pattern1 = "((https:\/\/)*(www.)*)((invidio.us)|(youtube.com))\/channel\/"
	channelID = newLink.split('/')[-1] if(newLink.split('/')[-1]!='') else newLink.split('/')[-2]
	newChRssLink = channelRssLink + channelID
	channelFeed = feedparser.parse(newChRssLink)
	if(channelFeed.get('status') == 200):
		addChannel(channelFeed)
	else:
		print('\n[!] Error, wrong Channel URL provided!\n'+newLink+'\n')

def addChannel(channelFeed):
	newC = {}
	channelName = channelFeed['feed']['title']
	newC['link'] = channelFeed['feed']['links'][1]['href']
	newC['feed'] = channelFeed['feed']['links'][0]['href']
	newC['id'] = channelFeed['feed']['yt_channelid']

	time_ = str(time.time()).split('.')[0]
	if(not os.path.isdir('BackUpChannels')):
		os.mkdir('BackUpChannels')
	try:
		copyfile('channels.json', 'BackUpChannels/channels_BACKUP_'+time_+'.json')
	except:
		#pass
		initFile = open('channels.json','w')
		# _tm = {}
		# json.dump(_tm,initFile,indent = 4, sort_keys=True)
		initFile.close()

	cha = open('channels.json','r')
	try:
		chaJson = json.load(cha)
		cha.close()
	except:
		chaJson = {}
	cha = open('channels.json','w')
	if(chaJson.get(channelName)):
		print('\n[~] Channel: '+channelName+' - already exists in file\n')
	else:
		chaJson[channelName] = newC
		print('\n[+] Channel: '+channelName+' - Added\n')
	json.dump(chaJson,cha,indent = 4, sort_keys=True)
	cha.close()

def latestVideoGrab():
	pass

'''
LOL, TODO main function
'''

def main():
	parser = argparse.ArgumentParser(description = "\033[92m[#] YouTube Video Grabber [#]\033[0m")
	parser.add_argument("-a", "--add", help="add channel flag; -a ", action="store_true")
	parser.add_argument("-u", "--url", help="channel url; -u <URL>", dest='churl')
	parser.add_argument("-f", "--lfile", help="channel urls file; -f <file path>", dest='fpath')
	args = parser.parse_args()



	if(len(sys.argv) == 1):
		print("\n\033[92m[+] Getting Latest Videos\033[0m\n ")
		latestVideoGrab()
		
	
	elif(args.add):
		if(args.churl):
			print("\n\033[93m[+] Adding New URL\033[0m\n ")
			newUrlAdd(args.churl)
		elif(args.fpath):
			print("\n\033[93m[+] Adding New URLs from File\033[0m\n ")
			ll = []
			with open(args.fpath,'r') as f:
				ll=f.readlines()
			fl = [l.replace('\n','') for l in ll]	# remove '\n' at end of each line
			for ffll in fl:
				newUrlAdd(ffll)
		else:
			print("\n\033[91m[-] Error!, did not provided URL or URLs list File \nSee -u or -f arguments\nSee help!\n\033[0m\n ")
			#parser.print_help()
	else:
		print("\n\033[91m[?] Cant figure it out, np. See help below:\033[0m\n ")	
		parser.print_help()
	


main()
