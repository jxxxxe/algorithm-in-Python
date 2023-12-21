from collections import deque

n=int(input())
a,b=map(int,input().split())
m=int(input())
relations=[set() for _ in range(n+1)]

for _ in range(m):
    x, y = map(int,input().split())
    relations[x].add(y)
    relations[y].add(x)

count=0
queue=deque([a])

while len(queue):
    size=len(queue)
    for _ in range(size):
        next=queue.popleft()
        if next == b:
            print(count)
            exit()
        for p in relations[next]:
            queue.append(p)
        relations[next]={}
    count+=1

print(-1)