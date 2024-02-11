#원래 수와 그 수를 변경한 걸 같이 프린트할 때 원래수를 따로 보존 해놓는거 잊지말기!!!
import sys
T=int(input())

for _ in range(T):
    A,B=map(int,sys.stdin.readline().split())
    a,b=A,B
    while b>0:
        if a<b:
            a,b=b,a
        a,b=b,a%b
    gcd=a
    print((A*B)//gcd)