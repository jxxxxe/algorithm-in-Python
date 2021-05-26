import sys

N=int(input())

list=list(map(int,sys.stdin.readline().split()))
list.sort()

for i in range(N):
    count=0
    for j in range(N):
        count+=abs(list[i]-list[j])
    if i==0:
        min=count
        present=list[i]
    elif min>count:
        min=count
        present=list[i]

print(present)