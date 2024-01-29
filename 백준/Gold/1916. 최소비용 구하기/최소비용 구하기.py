import sys
import heapq

input = sys.stdin.readline

n=int(input())
m=int(input())

bus = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    bus[s].append((e,c))

start_city, end_city = map(int, input().split())

def dijkstra(s,e):
    q = []
    heapq.heappush(q,(0,s))
    costs={}

    while q:
        cost, end = heapq.heappop(q)

        if end in costs and costs[end] < cost:
            continue

        if end == e:
            return cost

        for next_end, next_cost in bus[end]:
            total_cost = next_cost+cost
            if next_end not in costs or total_cost < costs[next_end]:
                costs[next_end] = total_cost
                heapq.heappush(q, (total_cost, next_end))

print(dijkstra(start_city, end_city))