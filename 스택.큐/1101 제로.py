#python은 스택의 자료구조를 지원하지 않으므로 리스트로 흉내를 낸다. => append, pop, list[-1](=top) 이용
#input=sys.stdin.readline으로 선언을 하면 앞으로 sys~대신에 input()으로 대체 가능하다

import sys
K=int(input())

list=[]
for _ in range(K):
    n=int(sys.stdin.readline().strip())
    if n!=0:
        list.append(n)
    else:
        list.pop()

print(sum(list))