#input은 시간이 어어엄청 오래 걸린다!(4344) sys를 이용하자!!
import sys

N,M=map(int,sys.stdin.readline().split())

dset=set()
for _ in range(N):
    dset.add(sys.stdin.readline().strip())

dblist=[]
for i in range(M):
    name=sys.stdin.readline().strip()
    if name in dset:
        dblist.append(name)

dblist.sort()
print(len(dblist))
for i in dblist:
    print(i)