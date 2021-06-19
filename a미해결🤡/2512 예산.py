import sys

N=int(input())
request=list(map(int,sys.stdin.readline().split()))
M=int(input())

if sum(request)<=M:
    print(max(request))
    exit()

request.sort()
div=M//N
for i in range(len(request)):
    if request[i]<=div:
        M-=request[i]
        div=M//(N-i)
    else:
        print(M//(N-i))
        break