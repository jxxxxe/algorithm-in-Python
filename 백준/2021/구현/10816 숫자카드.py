import sys

N=int(input())
card=list(map(int,sys.stdin.readline().split()))
M=int(input())
many=list(map(int,sys.stdin.readline().split()))

count={}
for c in card:
    if not c in count:
        count[c]=1
    else:
        count[c]+=1

for m in many:
    if m in count:
        print(count[m],end=' ')
    else:
        print(0,end=' ')