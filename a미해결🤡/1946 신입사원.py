import sys

T=int(input())

for _ in range(T):
    N=int(sys.stdin.readline())
    rank=[]
    count=N
    for _ in range(N):
        score,meet=map(int,sys.stdin.readline().split())
        rank.append((score,meet))

    i=0
    rsort_rank=sorted(rank)[::-1]
    for r in rsort_rank:
        i+=1
        for j in range(i,N):
            if r[1]>rsort_rank[j][1]:
                count-=1
                break
    print(count)