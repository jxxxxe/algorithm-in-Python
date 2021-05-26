#덱...이라..함은..앞과..뒤가..다..뚫려있어..어디로든..빠져나갈..수..있는..그런..것이지..그냥..큐라고..생각하면..된다..
#시간이 쫌 더 빠른 애들 코드를 보니 리스트를 써서 push_front/pop_front는 list.insert(0,x)/list.pop(0)으로 구현했더라
#ㅇㅅㅇ..그데 큐2에서는 리스트로는 시간초과 떠버림; 걍 deque를 계속 쓰기루 해~
#front/back은 list[0]/list[-1] => 이긴 했는데 back은 내 방법이 더 빨랐음 호호호
#n을 출력하는데 리스트 a가 비면 -1을 출력하라는 => print(n if a else -1) 을 썼음; (미친놈; 앞으로 유용하게 잘 쓰겠다;)

from collections import deque
import sys

N=int(input())

dq=deque()
for _ in range(N):
    line=sys.stdin.readline().split()
    op=line[0]
    if len(dq)<=0 and (op=='pop_front' or op=='pop_back' or op=='front' or op=='back'):
            print(-1)
            continue
    elif op=='push_front':
        dq.appendleft(line[1])
    elif op=='push_back':
        dq.append(line[1])
    elif op=='pop_front':
        print(dq.popleft())
    elif op=='pop_back':
        print(dq.pop())
    elif op=='size':
        print(len(dq))
    elif op=='empty':
        print(int(len(dq)==0))
    elif op=='front':
        print(dq[0])
    elif op=='back':
        print(dq[len(dq)-1])