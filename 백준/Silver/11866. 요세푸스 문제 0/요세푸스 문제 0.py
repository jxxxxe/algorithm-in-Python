from collections import deque
N, K = map(int, input().split())
rotate = deque([str(i+1) for i in range(N)])
answer = []

while len(answer)<N:
    count=1
    while count<K:
        rotate.append(rotate.popleft())
        count+=1
    else:
        answer.append(rotate.popleft())
    
print("<",end='')
print(', '.join(answer), end='>')