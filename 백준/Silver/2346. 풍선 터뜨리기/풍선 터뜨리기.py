from collections import deque

N=int(input())
balloons=deque(enumerate(map(int,input().split())))

answer = []

while balloons:
    [cur_idx, move] = balloons.popleft()
    answer.append(cur_idx+1)
    
    balloons.rotate(-(move-1) if move>0 else -move) 

print(*answer)