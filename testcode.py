#!/usr/bin/env python3
import urllib
import urllib.request
from urllib.parse import urlparse
import sys
#sys.tracebacklimit = 0

with open("./list.txt", "r") as f:
    url = f.read().split("\n")
urls = sorted(list(set(url)),key=url.index) # unique/sort

def response_check(url):
    try:
        f = urllib.request.urlopen(url)
        #print('OK:', url)
        print('OK!')
        f.close()
        return url
    except urllib.request.HTTPError:
        print('Not found:', url)

def parsed_url(url):
    parsed_url = urlparse(url)
    print(parsed_url.netloc)
    # 階層パス
    print(parsed_url.path) # /archives/
    
def url_decision(url):
    url = response_check(url)
    #判定
    parsed_url = urlparse(url)
    #print (parsed_url.netloc)
    
    #アドレス判定 twitter/pixiv/seiga
    if  (parsed_url.netloc == "twitter.com" or parsed_url.netloc == "www.pixiv.net" and parsed_url.path == "/member_illust.php" or parsed_url.netloc == "seiga.nicovideo.jp"):
        print("true")
        if (parsed_url.netloc == "twitter.com"):
            print("twitter")
        elif (parsed_url.netloc == "www.pixiv.net"):
            print("pixiv")
        elif (parsed_url.netloc == "seiga.nicovideo.jp"):
            print("seiga")
    else:
        print("false")

def get_tweet(url):

def get_pixiv(url):

def get_seiga(url):

for url in urls :
    print("-----------------")
    url_decision(url)


