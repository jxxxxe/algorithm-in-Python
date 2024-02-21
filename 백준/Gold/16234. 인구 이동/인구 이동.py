import sys
from collections import deque
sys.setrecursionlimit(10**6)


input = sys.stdin.readline

n,l,r = map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(n)]

pos=[[-1,0],[0,-1],[1,0],[0,1]]
answer=0

while True:
    mark=[[0 for _ in range(n)] for _ in range(n)]
    num=0
    dic={}

    def dfs(i,j,num):
        global mark
        global dic
        mark[i][j]=num
        if num not in dic:
            dic[num]=[0,0]
        dic[num][0]+=graph[i][j]
        dic[num][1]+=1

        for p in pos:
            ni, nj = i+p[0], j+p[1]
            if 0<=ni<n and 0<=nj<n and mark[ni][nj]==0 and l<=abs(graph[i][j]-graph[ni][nj])<=r:
                dfs(ni,nj,num)

    for i in range(n):
        for j in range(n):
            if mark[i][j]==0:
                num+=1
                dfs(i,j,num)

    if num==n*n:
        break

    answer+=1
    
    for i in range(n):
        for j in range(n):
            idx=mark[i][j]
            graph[i][j] = dic[idx][0] // dic[idx][1]

print(answer)