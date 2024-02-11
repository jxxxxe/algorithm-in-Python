#lambda를 이용해 내림차순 계산 => lambda x:-x[0]
import sys

N=int(input())

count={}
sum=0
for _ in range(N):
    x=int(sys.stdin.readline().strip())
    sum+=x
    if not x in count:
        count[x]=1
    else:
        count[x]+=1

count=sorted(count.items(),key=lambda x:x[0])
sort=sorted(count,key=lambda x:-x[1])

center=0
for i in range(len(count)):
    center+=count[i][1]
    if center>=N/2:
        center=count[i][0]
        break

print(round(sum/N))
print(center)
if len(sort)>=2 and sort[0][1]==sort[1][1]:
    print(sort[1][0])
else:
    print(sort[0][0])
print(count[len(count)-1][0]-count[0][0])