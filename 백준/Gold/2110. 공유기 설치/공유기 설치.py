import sys

input = sys.stdin.readline

n,c=map(int, input().split())
homes=sorted([int(input()) for _ in range(n)])

start, end = 1, homes[n-1]-homes[0]
answer=1
while start<=end:
    length=(start+end)//2 #거리를 이분탐색
    current = homes[0]
    count=1
    for i in range(1,n):
        if homes[i]>=current+length:
            count+=1
            current=homes[i]
    if count>=c:
        answer=length
        start=length+1
    else:
        end=length-1

print(answer)