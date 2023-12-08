import sys
from collections import deque

def next_append(x,y):
    if x>=0 and y>=0 and x<N and y<M and miro[x][y]:
        miro[x][y] = 0
        bfs.append([x, y])

N, M = map(int, sys.stdin.readline().split())

miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
answer = 0
bfs = deque([[0,0]])

while True:
    answer += 1
    size = len(bfs)
    for _ in range(size):
        cur_x, cur_y = bfs.popleft()
        if cur_x == N-1 and cur_y == M-1:
            print(answer)
            exit()
        next_append(cur_x+1, cur_y)
        next_append(cur_x, cur_y+1)
        next_append(cur_x-1, cur_y)
        next_append(cur_x, cur_y-1)