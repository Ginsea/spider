# -*- coding:utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

def parseurl(url):
    resdict = {}
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {
        'User-Agent': user_agent
    }

    html = ""

    try:
        req = urllib2.Request(url=url, headers=headers)
        res = urllib2.urlopen(req)
        html = res.read()
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print(e.code)
            exit(1)
        if hasattr(e,"reason"):
            print(e.reason)
            exit(1)

    subp = BeautifulSoup(html, "html.parser")

    for suba in subp.find_all("a"):
        if suba.find("h2"):
            author = suba.find("h2").find(text=True).strip().encode("utf-8")
            infos = suba.find_next("a")
            contents = infos.find("span").find(text=True).strip().encode("utf-8")
            if author in resdict.keys():
                continue
            else:
                resdict[author] = contents

    return resdict
