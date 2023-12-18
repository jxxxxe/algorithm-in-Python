S=input()
answer=""

count0,count1= S.count('0')//2,S.count('1')//2

for s in S:
    if s == '0' and count0>0:
        answer+='0'
        count0-=1
    elif s == '1' and count1>0:
        count1-=1
    elif s=='1' and count1==0:
        answer+='1'

print(answer)