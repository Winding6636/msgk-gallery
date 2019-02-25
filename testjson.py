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
params = {'id': '1078598675369144321','tweet_mode':'extended','include_entities':True}
#params = {'id': 1078598675369144321}
# -RestVerb 'GET' -Parameters @{"id"="1078598675369144321";"tweet_mode"="extended";"include_entities"="true""

print(twitter)
#result = twitter.post(url, params)
res = twitter.get(url, params = params)
res = json.loads(res.text)
print (res['full_text'],res['full_text'])