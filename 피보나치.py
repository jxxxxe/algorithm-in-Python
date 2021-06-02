import sys

T=int(input())

for _ in range(T):
    n=int(sys.stdin.readline().strip())
    count=[(1,0),(0,1)]
    for i in range(2,n+1):
        count.append((count[i-2][0]+count[i-1][0],count[i-2][1]+count[i-1][1]))

    print(count[n][0],count[n][1])