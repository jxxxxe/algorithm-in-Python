import sys
from collections import deque

input = sys.stdin.readline

n,m,k,x = map(int,input().split())

connect = [[] for _ in range(n+1)]
distance = [sys.maxsize]*(n+1)

for _ in range(m):
    start, end = map(int, input().split())
    connect[start].append(end)

q = deque([(0,x)])
distance[x]=0
result = []
while q:
    dist, end = q.popleft()

    if dist == k:
        result.append(str(end))
        continue

    for next_end in connect[end]:
        next_distance = dist+1
        if next_distance < distance[next_end]:
            distance[next_end] = next_distance
            q.append((next_distance,next_end))

print('\n'.join(sorted(result, key= lambda x: int(x))) if result else -1)