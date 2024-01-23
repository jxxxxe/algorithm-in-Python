import sys
import heapq

N = int(input())
heap= list(map(int,sys.stdin.readline().split()))
heapq.heapify(heap)

for _ in range(N-1):
    nums = list(map(int,sys.stdin.readline().split()))
    for num in nums:
        heapq.heappushpop(heap,num)

print(heap[0])