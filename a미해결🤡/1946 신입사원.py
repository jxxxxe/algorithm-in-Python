import sys

T=int(input())

for _ in range(T):
    N=int(sys.stdin.readline())
    rank=[]
    count=N
    for _ in range(N):
        score,meet=map(int,sys.stdin.readline().split())
        rank.append((score,meet))

    for i in range(1,N+1):
        for r in rank:
            if r[1]>i and r[0]>i:
                count-=1