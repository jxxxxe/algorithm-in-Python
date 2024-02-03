from collections import deque

n, k = map(int,input().split())

if n>k:
    print(n-k)
    exit()

def bfs():
    queue=deque([n])
    visit=set([n])
    time=0

    def can_go(x):
        if x not in visit and 0<=cur<=min(2*k,100000):
            queue.append(x)
            visit.add(x)

    while queue:
        for _ in range(len(queue)):
            cur=queue.popleft()

            if cur==k:
                print(time)
                exit()
            
            can_go(cur*2)
            can_go(cur+1)
            can_go(cur-1)

        time+=1

bfs()