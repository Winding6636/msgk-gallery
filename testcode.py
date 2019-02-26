#!/usr/bin/env python3
import urllib
import urllib.request
from urllib.parse import urlparse
from requests_oauthlib import OAuth1Session
import requests
import json
import os
from time import sleep
from datetime import datetime

with open('setting.json') as f:
    setting = json.load(f)

twitter = OAuth1Session(setting['Twitter_API']['CK'],setting['Twitter_API']['CS'],setting['Twitter_API']['AT'],setting['Twitter_API']['ATS'])
msgks = []

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
    result = 0
    parsed_url = urlparse(url)
    if (parsed_url.scheme):
        try:
            rc = urllib.request.urlopen(url)
            result = 1
            rc.close()
            return result,url,parsed_url
        except urllib.request.HTTPError:
            print('Not found:', url)
            return result,url,parsed_url
            
    else:
        print("URLですらないです.... `"+url+"`")
        return result,url,parsed_url
        

def get_tweet(url):
    code = 0
    print ("get_tweet")
    tweet_id = ((parsed_url.path.split('status/',1))[1])
    api = "https://api.twitter.com/1.1/statuses/show.json"
    params = {'id': tweet_id,'tweet_mode':'extended','include_entities':True}
    res = twitter.get(api, params = params)
    res = json.loads(res.text)

    ###
    f = open("output.json", "w")
    json.dump(res, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    
    print(res['extended_entities']['media'][0]['type'])
    print(res['created_at'])
    print(res['extended_entities']['media'][0]['media_url_https'])
    print(res['extended_entities']['media'][0]['sizes'])
    ###

    restype = (res['extended_entities']['media'][0]['type'])
    #resdata = (res['created_at'])
    #resimg = (res['extended_entities']['media'][0]['media_url_https'])

    if (restype == "photo"):
        #print("fetching image "+attachment["url"]+" ...")
        fname = url.replace("https://", "").replace("http://", "").replace("/", "_").replace("@", "")
        code = 1
    else:
        print ("NO Photo Image")
        fname = ""
        
    return code,res,fname

def get_pixiv(url):
    code = 0
    print ("pixiv_get")

    #print("fetching image "+attachment["url"]+" ...")
    res = ""
    jsonfile = ""
    return code,res,jsonfile

def get_seiga(url):
    print ("seiga_get")
    
    #print("fetching image "+attachment["url"]+" ...")
    res = ""
    jsonfile = ""
    return code,res,jsonfile

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
            print("twitter.com")
            code,res,fname = get_tweet(url)
        elif (parsed_url.netloc == "www.pixiv.net"):
            print("pixiv.net")
            code,res,jsonfile = get_pixiv(url)
        elif (parsed_url.netloc == "seiga.nicovideo.jp"):
            print("seiga.nico")
            code,res,jsonfile = get_seiga(url)
    else:
        print("非対応のURLです。対象のURLか確認してください。 -h ", url)
        continue

    if not code == 1:
        print("SKIP")
        continue
    cache_file_name = "cache/" + fname +".json"
#    if not os.path.exists(cache_file_name): #ファイル存在スルーをするかキャッシュとして
        #print("fetching "+url+" ...")
    with open(cache_file_name, "w") as f:
        json.dump(res, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
        print ("json save!")
    sleep(1)
    jsonf = json.load(open(cache_file_name))
    print ("json load!")
    
    #print (jsonf)

    if (fname.startswith("twitter.com")):
        print("jsonfile_twitter")
        img_list = jsonf['extended_entities']['media']
        for img_list in img_list:
            img_url = img_list['media_url_https']
            print (img_url)
            thumb_url = img_url + ":small"
            print (thumb_url)
            img_url = urlparse(img_url)
            print ((img_url.path).replace('/media/', ''))
            print (fname)

            print ("ThumbName: " + fname.replace('status_', '') + "_" + (img_url.path).replace('/media/', '').replace('.*','_s.*'))
            print ("CreateData: " + jsonf['created_at']) #作成日時
            print ("URL: " + img_list['expanded_url']) #ツイートURL

            msgks.append({
                "original": img_list['expanded_url'],
                "unix": datetime.strptime(jsonf['created_at'], "%a %b %d %H:%M:%S %z %Y").timestamp(),
                "origimg": img_list['media_url_https'],
                "thumbimg": thumb_url
            })

    elif (fname.startswith("www.pixiv.net")):
        print("jsonfile_pixiv")
        #get_pixiv(url)
    elif (fname.startswith("seiga.nicovideo.jp")):
        print("jsonfile_seiga")
        #get_seiga(url)


    msgks = sorted(msgks, key=lambda x:x["unix"], reverse = True)
    print (msgks)
    f = open("result.json", "w")
    json.dump(msgks, f, ensure_ascii=False, indent=4, separators=(',', ': '))
    f.close()

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

