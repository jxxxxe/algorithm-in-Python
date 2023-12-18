import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze=[[int(j) for j in sys.stdin.readline().strip()] for _ in range(N)]
queue=deque([[0,0]])

def bfs():
    count = 1
    while len(queue)>0:
        for _ in range(len(queue)):
            [x,y] = queue.popleft()
            if x==N-1 and y==M-1:
                return count
            if x>=0 and y>=0 and x<N and y<M and maze[x][y]==1:
                queue.append([x+1,y])
                queue.append([x,y+1])
                queue.append([x-1,y])
                queue.append([x,y-1])
                maze[x][y]=2
        count+=1

print(bfs())