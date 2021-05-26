import sys
N=int(input())
input=sys.stdin.readline

stack=[]
for _ in range(N):
    line=input().strip()
    if line[:4]=="push":
        stack.append(line[5:])
    elif line=="pop":
        if stack==[]: print(-1)
        else:        print(stack.pop())
    elif line=="size":
        print(len(stack))
    elif line=="empty":
        print(int(stack==[]))
    elif line=="top":
        if stack==[]:print(-1)
        else:       print(stack[-1])