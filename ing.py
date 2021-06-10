#2차원 배열 만들 때 [[0]*N]*N하면 나중에 배열 요소 넣을 때 모든 행이 같아짐;
import sys
N,M=map(int,input().split())

table=[[0 for _ in range(N)]for _ in range(N)]

for i in range(N):
    col=sys.stdin.readline().strip()
    for j in range(N):
        table[i][j]=int(col.split()[j])
    
print(table)