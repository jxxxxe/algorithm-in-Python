import sys

N=int(input())
list_a=list(map(int,sys.stdin.readline().split()))
M=int(input())
accums=[list_a[0]]

for i in range(1,N):
    accums.append(accums[i-1]+list_a[i])

for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    print(accums[b-1]-accums[a-2]) if a>1 else print(accums[b-1])