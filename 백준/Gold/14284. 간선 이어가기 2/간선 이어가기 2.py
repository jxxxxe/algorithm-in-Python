import sys
import heapq

input = sys.stdin.readline

n,m = map(int, input().split())
connects= [[] for _ in range(n+1)]

for _ in range(m):
    i,j,weight = map(int, input().split())
    connects[i].append((j,weight))
    connects[j].append((i,weight))

s,t = map(int, input().split())

q=[]
heapq.heappush(q,(0,s))
result = {s:0}

while q:
    weight, node = heapq.heappop(q)

    if node == t:
        print(result[t])
        break

    for connect in connects[node]:
        connect_node, connect_weight = connect
        if connect_node not in result or weight+connect_weight < result[connect_node]:
            result[connect_node] = weight+connect_weight
            heapq.heappush(q, (weight+connect_weight, connect_node))
    