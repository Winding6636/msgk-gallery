#!/usr/bin/env python3
import urllib
import urllib.request
from urllib.parse import urlparse
from requests_oauthlib import OAuth1Session
import requests
import json
import sys

#sys.tracebacklimit = 0

setting = json.load(open("setting.json"))

#print (setting['Twitter_API'])

twitter = OAuth1Session(setting['Twitter_API']['CK'],setting['Twitter_API']['CS'],setting['Twitter_API']['AT'],setting['Twitter_API']['ATS'])

url = "https://api.twitter.com/1.1/statuses/show.json"
#url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

#params = {'screen_name':'T_Winding','exclude_replies':True,'include_rts':False,'count':10}
params = {'id': '935671554523803648','tweet_mode':'extended','include_entities':True}
#params = {'id': 1078598675369144321}
# -RestVerb 'GET' -Parameters @{"id"="1078598675369144321";"tweet_mode"="extended";"include_entities"="true""

print(twitter)
#result = twitter.post(url, params)
res = twitter.get(url, params = params)
res = json.loads(res.text)
f = open("output.json", "w")
json.dump(res, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
#print (res)
print(res['created_at'])
print(res['extended_entities']['media'][0]['media_url_https'])
print(res['extended_entities']['media'][0]['sizes'])


tweeturl = "https://twitter.com/haguransan/status/1078598675369144321"
parsed_url = urlparse(tweeturl)
print (parsed_url.path)
print ("status" in parsed_url.path)
print (parsed_url.path.find('status/'))
split_url = (parsed_url.path.split('status/',1))
print (split_url[1])
print(res['extended_entities']['media'][0]['type'])
#print ("----------------------")
#print(res['extended_entities']['media'][0]['media_url_https'])
#print(res['extended_entities']['media'][1]['media_url_https'])
#print(res['extended_entities']['media'][2]['media_url_https'])
#print(res['extended_entities']['media'][3]['media_url_https'])
print ("----------------------")
#print (res['extended_entities']['media'][]['media_url_https'])

img_list = res['extended_entities']['media']
for imgdl in img_list:
    img_url = imgdl['media_url_https']
    print (img_url)
