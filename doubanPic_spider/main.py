# -*- coding: utf-8 -*-
# __author__ = 'Heisenbean'
import os
import re
import requests
import urllib2
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


index = 0
base_url = raw_input('请输入豆瓣相册地址:')
url = base_url + '?start=0'
html = urllib2.urlopen(url).read()

#match pics
imagesList = []
soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
node = soup.find_all('div', {'class': 'photo_wrap'})

while node:   #no photos
    imagesList.append(url)
    index += 1
    url = base_url + '?start=' + str(index * 18)
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    node = soup.find_all('div', {'class': 'photo_wrap'})

if not os.path.exists('pic'):
    j = 0
    for url in imagesList:
        html = urllib2.urlopen(url).read()
        # init picsList
        pic_url = []
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        node = soup.find_all('div', {'class': 'photo_wrap'})
        for imageUrl in node:
            for l in imageUrl.find_all('img'):
                pic_url.append(l.get('src'))
        j+=1
        i = 0
        # create folder
        if not os.path.exists('pic'):
            print '##开始下载.共' + str(imagesList.__len__() - 1) + '页##'
            os.makedirs('pic')

        for url in pic_url:
            largeImg_url = url.replace('thumb', 'large')
            print '下载中...' + str(j) + '-' + str(i)
            pic = requests.get(largeImg_url)
            fp = open(os.getcwd() + '/pic/' + str(j) + '-' + str(i) + '.jpg', 'wb')
            fp.write(pic.content)
            fp.close()
            i += 1
            if i == pic_url.__len__():
                print '##第' + str(j) + '页下载完毕!!##'
else:
    print '已下载过了!'