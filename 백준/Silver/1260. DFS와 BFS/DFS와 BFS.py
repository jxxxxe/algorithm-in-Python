import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
links = [set() for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    links[a].add(b)
    links[b].add(a)

for i in range(N):
    links[i+1]=list(links[i+1])
    links[i+1].sort()

def dfs(result: list):
    for i in links[result[-1]]:
        if i not in result:
            result.append(i)
            dfs(result)
        
    return result
    
def bfs(result: list):
    queue = deque([result[0]])
    while queue and len(result)<N:
        size = len(queue)
        for _ in range(size):
            next=queue.popleft()
            for n in links[next]:
                if not n in result:
                    result.append(n)
                    queue.append(n)

    return result
    

print(*dfs([V]))
print(*bfs([V]))