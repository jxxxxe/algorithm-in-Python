from collections import deque

N,K=map(int,input().split())

queue=deque([i+1 for i in range(N)])

list=[]
while queue!=deque([]):
    for _ in range(K-1):
        queue.append(queue.popleft())
    list.append(queue.popleft())

print(list)