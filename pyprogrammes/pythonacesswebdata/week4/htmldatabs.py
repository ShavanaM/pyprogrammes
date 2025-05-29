
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)



import re
import urllib.request,urllib.parse,urllib.error
lstno=list()
fhand=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1502437.html')
for line in fhand:
    words=line.decode()
    num=re.findall('[0-9]+',words)
    for x in num:
        if int(x)>0:
            lstno.append(x)
ans=0
for n in lstno:
    ans=ans+int(n)
print(ans-8)
