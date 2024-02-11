import sys

N=int(input())
list=[]
score=0

for _ in range(N):
    list.append(int(sys.stdin.readline().strip()))

index=len(list)
while index>=0:
    score+=index
    index-=2 if list[index-1]<list[index-2]