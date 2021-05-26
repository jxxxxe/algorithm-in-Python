#시간초과
import sys

N=int(input())
list=list(map(int,sys.stdin.readline().split()))
M=int(input())

for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    print(sum(list[a-1:b]))