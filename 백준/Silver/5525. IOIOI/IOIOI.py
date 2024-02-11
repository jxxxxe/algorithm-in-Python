n=int(input())
m=int(input())
s=input()

i=0
result=0
while i<m:
    target="I"+"OI"*n
    i=s.find(target,i)
    if i==-1:
        break
    result+=1
    i+=len(target)
    while i<m-1 and s[i:i+2]=="OI":
        result+=1
        i+=2

print(result)