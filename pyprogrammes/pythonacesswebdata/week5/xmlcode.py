import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_1502439.xml'

uh = urllib.request.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)
lst=tree.findall('comments/comment')

count=0
num=0
for item in lst:
    num=item.find('count').text
    count=count+int(num)
print(count)
