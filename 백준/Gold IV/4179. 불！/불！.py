import sys
from collections import deque

input=sys.stdin.readline

r, c = map(int, input().split())
graph=[]
jpos=[]
fpos=[]
for i in range(r):
    line=input().strip()

    jx=line.find("J")
    if jx!=-1:
        jpos=[i,jx]

    for idx,l in enumerate(line):
        if l=="F":
            fpos.append([i,idx])

    graph.append(list(line))

fq=deque(fpos) if fpos else []
jq=deque([jpos])

iidx=[-1,0,1,0]
jidx=[0,-1,0,1]

count=0
while fq or jq:
    count+=1
    for _ in range(len(fq)):
        fi, fj = fq.popleft()
        for k in range(4):
            ni, nj = fi+iidx[k], fj+jidx[k]
            if 0<=ni<r and 0<=nj<c and graph[ni][nj]!="#" and graph[ni][nj]!="F":
                graph[ni][nj] = "F"
                fq.append([ni,nj])

    for _ in range(len(jq)):
        ji, jj = jq.popleft()
        for k in range(4):
            ni, nj = ji+iidx[k], jj+jidx[k]
            if not (0<=ni<r and 0<=nj<c):
                print(count)
                exit()
            if graph[ni][nj]==".":
                graph[ni][nj] = "J"
                jq.append([ni,nj])

print("IMPOSSIBLE")