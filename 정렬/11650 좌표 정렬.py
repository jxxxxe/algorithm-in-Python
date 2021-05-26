import sys

N=int(input())

list=[]
for _ in range(N):
    x,y=map(int,sys.stdin.readline().split())
    list.append((x,y))

list=sorted(list,key=lambda x:(x[0],x[1]))

for l in list:
    print("%s %s"%(l[0],l[1]))