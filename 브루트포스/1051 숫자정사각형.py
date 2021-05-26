#2차원 배열은 [[]]로 선언~!!
#사실 감으로 짜서 맞추긴 했는데 갓벽하게 이거다!싶진 않았음..쩝.. 공부하다보면 나아지겠지 뭐..
import sys

N,M=map(int,input().split())
rect=[[0 for i in range(M)]for j in range(N)]

for i in range(N):
    b=sys.stdin.readline().strip()
    for j in range(M):
        rect[i][j]=int(b[j])

n=min(N,M)
while n>0:
    for i in range(N-n+1):
        for j in range(M-n+1):
            if rect[i][j]==rect[i][j+n-1]==rect[i+n-1][j]==rect[i+n-1][j+n-1]:
                print(n*n)
                exit()
    n-=1

print(1)