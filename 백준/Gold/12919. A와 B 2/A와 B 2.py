from collections import deque

s=input()
t=input()

queue=deque([t])
while queue:
    for _ in range(len(queue)):
        str=queue.popleft()

        if str == s:
            print(1)
            exit()

        if len(str)==len(s):
            continue

        if str[-1]=="A":
            queue.append(str[:-1])
        if str[0] == "B":
            queue.append(str[:0:-1])

print(0)