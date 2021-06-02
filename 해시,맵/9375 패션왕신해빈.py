from collections import defaultdict
import sys

T=int(input())
for _ in range(T):
    N=int(sys.stdin.readline())
    wear=defaultdict(int)
    for _ in range(N):
        name,type=sys.stdin.readline().split()
        wear[type]+=1
    
    count=1
    for w in wear.values():
        count*=w+1
    print(count-1 if N else 0)