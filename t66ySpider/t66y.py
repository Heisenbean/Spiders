# -*- coding: utf-8 -*-
# __author__ = 'Heisenbean'

import os
import re
import urllib2
import requests

site= "http://t66y.com/htm_data/7/1611/2124550.html"
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(site, headers = header)

try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()

content = page.read()
result = unicode(content, 'GBK').encode('UTF-8')

contents = re.findall('<div class="c"></div>(.*?)<font color',result,re.S)[0]

picUrls = re.findall('img src=\'(.*?)\' onclick',contents)

i = 0
if not os.path.exists('pic'):
    os.makedirs('pic')
    for url in picUrls:
        print ' 共'+ str(picUrls.__len__()) +'张/' + '正在下载第' + str(i + 1) + '张'
        pic = requests.get(url)
        fp = open(os.getcwd() + '/pic/' + str(i) + os.path.splitext(url)[1], 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
        if i == picUrls.__len__():
            print '下载完毕!'
print('您已下载过了')