#이상한거시.. for문 인덱스인 i는 for문 밖에선 값이 없음;
import sys

N=int(input())
list=list(map(int,sys.stdin.readline().split()))
stack=[]

for i in range(N-1):
    for j in range(i+1,N):
        if list[i]<list[j]:
            stack.append(list[j])
            break
    if len(stack)<=i:
        stack.append(-1)

stack.append(-1)
for s in stack:
    print(s,end=' ')