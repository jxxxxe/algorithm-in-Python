import sys
T=int(input())
counts=[]

for _ in range(T):
    a,b=map(int,sys.stdin.readline().split())
    sum=0
    count=0
    maxnum=1

    if b-a<=3:
        counts.append(b-a)
        continue

    for i in range(1,b):
        if sum+i > b-a:
            maxnum=i-1
            sum-=maxnum
            count-=1
            break
        sum+=i*2
        count+=2

    while sum<b-a:
        if sum+maxnum>b-a:
            maxnum-=1
            continue
        sum+=maxnum
        count+=1

    counts.append(count)

for c in counts:
    print(c)