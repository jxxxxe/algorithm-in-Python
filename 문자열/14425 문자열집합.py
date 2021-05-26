import sys

N,M=map(int,input().split())
strset=set()

for _ in range(N):
    strset.add(sys.stdin.readline())

count=0
for _ in range(M):
    if sys.stdin.readline() in strset:
        count+=1

print(count)