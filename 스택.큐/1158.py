N,K=map(int,input().split())

list=[]
plist=[]
for i in range(N):
    list.append(i+1)

i=0
index=0
count=0
while i<N:
    if list[index%N]!=0: #예시에 맞춰 인덱스를 숫자로 넣는 실수는 하지 말 것!!!!
        count+=1
    if count==K:
        plist.append(list[index%N])
        list[index%N]=0
        count=0
        i+=1
    index+=1

print("<",end='')
for j in plist:
    print(str(j),end='')
    if j!=plist[len(plist)-1]:
        print(", ",end='')
print(">")