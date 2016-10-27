
import os
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

f = open('source.txt','r')
html = f.read()
f.close()

#match pics

large = re.findall('"photolst clearfix">(.*?)<div id="link-report',html,re.S)[0]
pic_url = re.findall('img src="(.*?)" /',large)
i = 0
# create folder
os.makedirs('pic')

for url in pic_url:
    largeImg_url = url.replace('thumb','large')
    print 'now downloading...' + largeImg_url
    pic = requests.get(largeImg_url)
    fp = open(os.getcwd() + '/pic/' + str(i) + '.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i += 1
    if i == pic_url.__len__():
        print '##donwload completed!##'
