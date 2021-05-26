import sys
from collections import deque

N=int(input())

q=deque()
for _ in range(N):
    line=sys.stdin.readline().split()
    op=line[0]
    if op=="push": q.append(line[1])
    elif op=="pop": print(q.popleft() if q else -1)
    elif op=="size": print(len(q))
    elif op=="empty": print(0 if q else 1)
    elif op=="front": print(q[0] if q else -1)
    elif op=="back": print(q[len(q)-1] if q else -1)