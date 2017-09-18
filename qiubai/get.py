# -*- coding:utf-8 -*-

import os
import sys
import time
from parse import parseurl
import argparse

def opt():
    args = argparse.ArgumentParser(description="spider infos from qiushibaike web")
    args.add_argument("-p", "--pages", help="The number of pages you want to get", default=10)
    args.add_argument("-o", "--ouf", help="The output file", default="qiushibaike.txt")
    return args.parse_args()

def main():
    args = opt()
    pages = args.pages
    ouf = args.ouf

    url = "http://www.qiushibaike.com/hot/page/{}"

    finaldict = {}

    i = 1
    while i < int(pages):
        sys.stdout.write("loading the {}th page\n".format(i))
        newurl = url.format(i)
        subdict = parseurl(url=newurl)
        with open(ouf, "a") as ouhandle:
            for subkeys in subdict.keys():
                ouhandle.write("{}\t\t{}\n".format(subkeys, subdict[subkeys]))
        finaldict.update(subdict)
        time.sleep(10)
        i += 1

if __name__ == '__main__':
    main()