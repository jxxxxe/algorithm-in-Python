import sys

T=int(input())

for _ in range(T):
    N,rank=int(sys.stdin.readline()),[]
    for _ in range(N):
        score,meet=map(int,sys.stdin.readline().split())
        rank.append((score,meet))

    rank.sort()
    min,count=rank[0][1],N
    for r in rank:
        if r[1]>min:
            count-=1
        else:
            min=r[1]
            
    print(count)