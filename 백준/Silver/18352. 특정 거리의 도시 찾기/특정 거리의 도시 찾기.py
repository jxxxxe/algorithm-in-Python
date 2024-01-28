import sys
from collections import deque

input = sys.stdin.readline

n,m,k,x = map(int,input().split())

connect = [[] for _ in range(n+1)]
distance = {}

for _ in range(m):
    start, end = map(int, input().split())
    connect[start].append(end)

q = deque([x])
distance[x]=0
result = []
while q:
    end = q.popleft()

    if distance[end] == k:
        result.append(end)
        continue

    for next_end in connect[end]:
        if next_end not in distance:
            distance[next_end] = distance[end]+1
            q.append(next_end)

print('\n'.join(list(map(str,sorted(result)))) if result else -1)