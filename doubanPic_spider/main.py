# -*- coding: utf-8 -*-
# __author__ = 'Heisenbean'
import os
import re
import requests
import urllib2
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

html = urllib2.urlopen("https://www.douban.com/photos/album/127041026").read()

#match pics

large = re.findall('"photolst clearfix">(.*?)<div id="link-report',html,re.S)[0]
pic_url = re.findall('img src="(.*?)" /',large)
i = 0
# create folder
if not os.path.exists('pic'):
    print '开始下载...'
    os.makedirs('pic')
    for url in pic_url:
        largeImg_url = url.replace('thumb','large')
        print '下载中...' + largeImg_url
        pic = requests.get(largeImg_url)
        fp = open(os.getcwd() + '/pic/' + str(i) + '.jpg','wb')
        fp.write(pic.content)
        fp.close()
        i += 1
        if i == pic_url.__len__():
            print '##下载完毕!##'