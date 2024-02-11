import sys

T=int(input())

for _ in range(T):
    N=int(input())
    note1=set(map(int,sys.stdin.readline().split()))
    M=int(input())
    note2=list(map(int,sys.stdin.readline().split()))
    for n in note2: print(int(n in note1))