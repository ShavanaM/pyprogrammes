import re
lstno=list()
fhand=open('regex_sum_1502435.txt')
for line in fhand:
    num=re.findall('[0-9]+',line)
    for x in num:
        if int(x)>0:
            lstno.append(x)
ans=0
for n in lstno:
    ans=ans+int(n)
print(ans)
