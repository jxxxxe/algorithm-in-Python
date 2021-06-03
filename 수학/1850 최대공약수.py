#https://www.acmicpc.net/problem/1850
A,B=map(int,input().split())

while B>0:
    if A<B:
        A,B=B,A
    A,B=B,A%B

for _ in range(A):
    print(1,end='')