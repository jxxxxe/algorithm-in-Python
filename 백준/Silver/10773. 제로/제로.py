import sys
K=int(input())

list=[]
for _ in range(K):
    n=int(sys.stdin.readline().strip())
    if n!=0:
        list.append(n)
    else:
        list.pop()

print(sum(list))