import sys
import heapq

input = sys.stdin.readline

N, D = map(int, input().split())
roads = [[] for _ in range(D+1)] #각 스타트(key)에서 어떤 지점(vaule[0])까지 걸리는 시간(value[1])
distance = [sys.maxsize]*(D+1) #0부터 각 지점(index)까지 걸리는 거리

for i in range(D):
    roads[i].append((i+1,1))

for _ in range(N):
    start, end, diff = map(int, input().split())
    
    if end>D or end-start<=diff:
        continue

    if not (start,end) in roads or roads[(start, end)]>diff:
        roads[start].append((end, diff)) #도착지, 차이


q=[]
heapq.heappush(q,(0,0)) #0부터 걸리는 거리, 도착지
distance[0] = 0

while q:
    dist, end = heapq.heappop(q)

    if dist > distance[end]:
        continue

    for i in roads[end]:
        next_end, next_diff = i[0], i[1]
        next_distance = dist+next_diff
        if next_distance < distance[next_end]:
            distance[next_end] = next_distance
            heapq.heappush(q,(next_distance, next_end))


print(distance[D])