# deque는 슬라이싱을 할 수 없다
# len 이용하기 전 갯수를  입력으로 받는지 여부를 잘 판단하자. len이 정확한 원소개수를 돌려주지 않을 수 있음
# 출력형식이 [,,,]이면 [, , ,]는 틀린 것이다.
# 뒤집는 연산은 시간이 많이 든다. 매번 앞 원소를 제거하는 것이므로 reverse 후 D는 맨 뒤 원소를 뽑는 것으로 대체할 수 있고 reverse는 마지막에 몰아서 처리한다.

import sys
from collections import deque

T=int(input())

for _ in range(T):
    p=list(sys.stdin.readline().strip())
    N=int(sys.stdin.readline().strip())
    xrr=deque((sys.stdin.readline().strip())[1:-1].split(','))
    if N<p.count('D'):
        print('error')
        continue
    if N==0:
        print("[]")
        continue
    
    rever=0
    for i in range(len(p)):
        if p[i]=='D':
            if rever%2==0:
                xrr.popleft()
            else:
                xrr.pop()
        elif p[i]=='R':
            rever+=1
    
    if rever%2==1:
        xrr.reverse() 
        
    printrr='['+','.join(xrr)+']'
    print(printrr)