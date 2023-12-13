import sys
from collections import deque

N = int(input())

q_or_s = list(map(int,sys.stdin.readline().split()))
values = list(map(int,sys.stdin.readline().split()))
M = int(input())
C = list(map(int,sys.stdin.readline().split()))
answer = []

queue = deque()

for i, value in enumerate(values):
    if q_or_s[i] == 0:
        queue.append(value)

for c in C:
    queue.appendleft(c)
    answer.append(str(queue.pop()))

print(' '.join(answer))