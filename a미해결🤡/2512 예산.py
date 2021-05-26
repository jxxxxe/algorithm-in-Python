import sys

N=int(input())
request=list(map(int,sys.stdin.readline()))
M=int(input())

if sum(request)<=M:
    print(max(request))
    exit()

