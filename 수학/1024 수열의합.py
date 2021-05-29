#https://www.acmicpc.net/problem/1024
N,L=map(int,input().split())

sum_i=sum(range(L))
for n in range(L,101):
    x=(N-sum_i)/n
    if x<0:
        break
    if x==int(x):
        for r in range(int(x),int(x+n)):
            print(r,end=' ')
        exit()
    sum_i+=n

print(-1)