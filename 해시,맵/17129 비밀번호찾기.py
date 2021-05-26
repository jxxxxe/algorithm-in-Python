import sys

N,M=map(int,input().split())

spwd={}
for _ in range(N):
    site,pwd=sys.stdin.readline().split()
    spwd[site]=pwd

for _ in range(M):
    site=sys.stdin.readline().strip()
    print(spwd[site])