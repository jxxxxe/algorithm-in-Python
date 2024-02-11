# #이상한거시.. for문 인덱스인 i는 for문 밖에선 값이 없음;
import sys

N,num=int(input()),list(map(int,sys.stdin.readline().split()))
wait,oken=[],{}
for i,n in enumerate(num):
    while wait and n>wait[-1][1]:
        oken[wait[-1][0]]=n
        wait.pop()
    wait.append((i,n))

for i in range(N):
    print(oken[i] if i in oken else -1 ,end=' ')