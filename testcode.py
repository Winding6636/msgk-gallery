#!/usr/bin/env python3
import urllib
import urllib.request
from urllib.parse import urlparse
from requests_oauthlib import OAuth1Session
import requests
import json
import os

with open('setting.json') as f:
    setting = json.load(f)

twitter = OAuth1Session(setting['Twitter_API']['CK'],setting['Twitter_API']['CS'],setting['Twitter_API']['AT'],setting['Twitter_API']['ATS'])

with open('./list.txt') as f:
    f.seek(0, os.SEEK_END)
    if f.tell():
        f.seek(0)
        url = f.read().split("\n")
        urls = sorted(list(set(url)),key=url.index) # unique/sort
    else:
        print ("list.txtが空です。")
        exit ()

def response_check(url):
    parsed_url = urlparse(url)
    if (parsed_url.scheme):
        try:
            rc = urllib.request.urlopen(url)
            result = 1
            rc.close()
            return result,url,parsed_url
        except urllib.request.HTTPError:
            print('Not found:', url)
            result = 0
            return result,url,parsed_url
            
    else:
        print("URLですらないです.... `"+url+"`")
        result = 0
        return result,url,parsed_url
        

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
    #url_decision(url)

    result,url,parsed_url = response_check(url)
    if not result == 1:
        continue   
    #アドレス判定 twitter/pixiv/seiga
    if  (parsed_url.netloc == "twitter.com" or parsed_url.netloc == "www.pixiv.net" and parsed_url.path == "/member_illust.php" or parsed_url.netloc == "seiga.nicovideo.jp"):
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
        print("非対応のURLです。対象のURLか確認してください。 -h ", url)



##未実装未精査json->html書き出し
from pyjade.parser import Parser
from pyjade.ext.html import HTMLCompiler, local_context_manager

def process(jade_string, context=None, **compiler_kwargs):
    ctx = context or {}
    block = Parser(jade_string).parse()
    compiler = HTMLCompiler(block, **compiler_kwargs)
    with local_context_manager(compiler, ctx):
        return compiler.compile()

#with open("base.pug", "r") as f_pug:
#    html = process(f_pug.read(), {"akanes": akanes})
#    with open("index.html", "w") as f_html:
#        f_html.write(html)
#with open("list.json", "w") as f:
#    json.dump(akanes, f)

