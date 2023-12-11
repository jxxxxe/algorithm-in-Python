import sys
from collections import deque

N=int(input())
queue=deque()
for _ in range(N):
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        queue.appendleft(command[1])
    elif command[0] == 2:
        queue.append(command[1])
    elif command[0] == 3:
        print(queue.popleft() if queue else -1)
    elif command[0] == 4:
        print(queue.pop() if queue else -1)
    elif command[0] == 5:
        print(len(queue))
    elif command[0] == 6:
        print(0 if queue else 1)
    elif command[0] == 7:
        print(queue[0] if queue else -1)
    elif command[0] == 8:
        print(queue[-1] if queue else -1)