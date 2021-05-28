#https://www.acmicpc.net/problem/18870
#set도 sorted 할 수 있다.

N=int(input())
spot=list(map(int,input().split()))
count={}

for i,s in enumerate(sorted(set(spot))):
    count[s]=i

for s in spot:
    print(count[s],end=' ')