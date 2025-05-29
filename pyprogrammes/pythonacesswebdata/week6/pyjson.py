import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_1502440.json'

uh = urllib.request.urlopen(url)
data = uh.read()

info = json.loads(data)
sum=0

for item in info["comments"]:
    sum=sum+int(item['count'])
print(sum)
