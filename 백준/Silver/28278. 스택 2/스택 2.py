import sys 

N = int(input())
stack = []

for _ in range(N):
    num = list(map(int, sys.stdin.readline().split()))
    if num[0] == 1:
        stack.append(num[1])
    elif num[0] == 2:
        print(stack.pop() if stack else -1)
    elif num[0] == 3:
        print(len(stack))
    elif num[0] == 4:
        print(0 if len(stack) else 1)
    elif num[0] == 5:
        print(stack[-1] if stack else -1)
        