# -*- coding: utf-8 -*-
# __author__ = 'Heisenbean'
import os
import re
import requests
import urllib2
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# file = open('source.html','r')
# html = file.read()
# file.close()

# soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')



index = 0
first_url = 'https://www.douban.com/photos/album/153337648/'
first_html = urllib2.urlopen(first_url).read()

#match pics
soup = BeautifulSoup(first_html,'html.parser',from_encoding='utf-8')
# node = soup.find_all('div', {'class': 'photo_wrap'})
# for imageUrl in node:
#     for l in imageUrl.find_all('img'):
#         print l.get('src')


# first_images = re.findall('"photolst clearfix">(.*?)<div id="link-report',first_html,re.S)[0]
# first_image = first_images.strip()

imagesList = []
node = soup.find_all('div', {'class': 'photo_wrap'})

while node:   #no photos
    url = first_url + '?start=' + str(index * 18)
    html = urllib2.urlopen(url).read()
    # image = re.findall('"photolst clearfix">(.*?)<div id="link-report',html,re.S)[0]
    # first_image = image.strip()
    # pic_url = re.findall('img src="(.*?)" /',image)
    node = soup.find_all('div', {'class': 'photo_wrap'})
    for imageUrl in node:
        for url in imageUrl.find_all('img'):
            imagesList.append(url)
    index += 1

if not os.path.exists('pic'):
    j = 0
    for url in imagesList:
        html = urllib2.urlopen(url).read()
        # match pics
        large = re.findall('"photolst clearfix">(.*?)<div id="link-report', html, re.S)[0]
        pic_url = re.findall('img src="(.*?)" /', large)
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


