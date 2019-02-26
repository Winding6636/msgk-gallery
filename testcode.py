#!/usr/bin/env python3
import urllib
import urllib.request
from urllib.parse import urlparse
from requests_oauthlib import OAuthSession, OAuth
import requests
import json
import sys

setting = json.load(open("setting.json"))

if (setting['debug'] == 1):
    print (':-: debug mode :-:')
    sys.tracebacklimit = 0

#twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理
    print (setting)
    print (sys.tracebacklimit)

with open("./list.txt", "r") as f:
    url = f.read().split("\n")
urls = sorted(list(set(url)),key=url.index) # unique/sort

#ENVCK
def env_check():
    print(hoge)
    #各サイトチェック res
    #TwitterAPI認証チェック

def response_check(url):
    try:
        f = urllib.request.urlopen(url)
        #print('OK:', url)
        print('OK!')
        f.close()
        return url
    except urllib.request.HTTPError:
        print('Not found:', url)

def url_decision(url):
    url = response_check(url)
    #判定
    parsed_url = urlparse(url)
    #print (parsed_url.netloc)
    
    #アドレス判定 twitter/pixiv/seiga
    if  (parsed_url.netloc == "twitter.com" or parsed_url.netloc == "www.pixiv.net" and parsed_url.path == "/member_illust.php" or parsed_url.netloc == "seiga.nicovideo.jp"):
        print("true")
        print("fetching "+url+" ...")
        if (parsed_url.netloc == "twitter.com"):
            print("twitter")
            #get_tweet(url)
        elif (parsed_url.netloc == "www.pixiv.net"):
            print("pixiv")
            #get_pixiv(url)
        elif (parsed_url.netloc == "seiga.nicovideo.jp"):
            print("seiga")
            #get_seiga(url)
    else:
        print("アドレス判定によりブロックされました。対象のURLか確認してください。 -h ", url)

def get_tweet(url):
    print ("twitter")
    
    print("fetching image "+attachment["url"]+" ...")

def get_pixiv(url):
    print ("pixiv")

    print("fetching image "+attachment["url"]+" ...")

def get_seiga(url):
    print ("seiga")
    print("fetching image "+attachment["url"]+" ...")

def thumbdl(imgurl):
    #thumbダウンロード
    print("saveing image "+attachment["url"]+" ...")

def jsonmatome(result):
    #収集結果をまとめる
    print("output json "+attachment["url"]+" ...")


for url in urls :
    print("-----------------")
    url_decision(url)


##未実装未精査json->html書き出し
from pyjade.parser import Parser
from pyjade.ext.html import HTMLCompiler, local_context_manager

def process(jade_string, context=None, **compiler_kwargs):
    ctx = context or {}
    block = Parser(jade_string).parse()
    compiler = HTMLCompiler(block, **compiler_kwargs)
    with local_context_manager(compiler, ctx):
        return compiler.compile()

with open("base.pug", "r") as f_pug:
    html = process(f_pug.read(), {"akanes": akanes})
    with open("index.html", "w") as f_html:
        f_html.write(html)
with open("list.json", "w") as f:
    json.dump(akanes, f)

