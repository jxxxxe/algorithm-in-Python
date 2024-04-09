import heapq
import sys

input = sys.stdin.readline

answers=[]
pi=[0,1,0,-1]
pj=[1,0,-1,0]

while True:
    n=int(input())

    if n==0:
        break

    miro=[list(map(int,input().split())) for _ in range(n)]

    dists=[[sys.maxsize for _ in range(n)] for _ in range(n)]
    dists[0][0]=miro[0][0]

    q=[]
    heapq.heappush(q,[miro[0][0],(0,0)])
    while True:
        dist, ij = heapq.heappop(q)
        i, j =ij

        if i==n-1 and j==n-1:
            answers.append(dist)
            break
        
        if dists[i][j]<dist:
            continue

        for k in range(4):
            ni, nj = i+pi[k], j+pj[k], 
            if 0<=ni<n and 0<=nj<n and miro[ni][nj]+dist < dists[ni][nj]:
                ndist = miro[ni][nj]+dist
                dists[ni][nj]=ndist
                heapq.heappush(q,[ndist,(ni,nj)])


[print(f'Problem {i+1}: {answers[i]}') for i in range(len(answers))]