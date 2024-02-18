import sys

input = sys.stdin.readline

n=int(input())
build=[-1]*500000
xlist=[]

for _ in range(n):
    x,y=map(int,input().split())
    build[x]=y
    xlist.append(x)

xlist.sort()

stack=[]
count=0

for x in xlist:
    while stack and stack[-1]>build[x]:
        stack.pop()
    if build[x] and (not stack or stack[-1]<build[x]):
        stack.append(build[x])
        count+=1

        
print(count)