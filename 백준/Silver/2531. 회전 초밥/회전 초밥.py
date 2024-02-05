import sys
input=sys.stdin.readline
n,d,k,c = map(int,input().split())

sushies=[]
for _ in range(n):
    sushi=int(input())
    sushies.append(sushi)

sushies.extend(sushies[:k])
result=0
for start in range(n):
    susi_set=set(sushies[start:start+k])
    count = len(susi_set)
    if c not in susi_set:
        count+=1
    result=max(result,count)

print(result)