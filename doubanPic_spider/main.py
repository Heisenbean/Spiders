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
for url in pic_url:
    print 'now downloading...' + url
    pic = requests.get(url)
    fp = open('pic' + str(i) + '.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i += 1