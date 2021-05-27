# 시도1) 리스트에 insert(index,)로 했더니 시간초과
# 시도2) 시도1에서 리스트->deque로 변경함으로써 맨 앞에 insert/delete 해야할 땐 appendleft/popleft를 씀. 그 외는 동일.
#       =>성공은 했지만 속도가 남들보다 4~5배 차이남
# 시도3,다른 사람 풀이 참고) 알파벳 담을 곳을 한개가 아닌 두개로 둔다. index는 필요없다.
#       <가 입력되므로써 커서 오른쪽에 있게 된 알파멧은 right에, >가 입력되면 right에 있던 애를 다시 왼쪽으로 넣는다
#       => 경우의 수가 줄어듦으로써 코드가 간결해짐, 편의를 위해 right는 리스트 대신 deque를 씀
# 찐막) for문 대신 join을 이용해서 리스트를 한 문자열로 이어서 출력하니 속도가 확 줄었다. right도 deque대신 list를 쓰면 속도가 좀 덜 나감. 
#       .reverse()는 .sort()처럼 제자리 연산이고, reversed(리스트)는 sorted(리스트)처럼 새로운 리스트를 반환한다.

import sys
from collections import deque
T=int(input())

for _ in range(T):
    key=sys.stdin.readline().strip()
    left,right=[],deque()
    for k in key:
        if k=='<' and left:
            right.appendleft(left.pop())
        elif k=='>' and right:
            left.append(right.popleft())
        elif k=='-' and left:
            left.pop()
        elif k!='<' and k!='>' and k!='-':
            left.append(k)
    print(''.join(left)+''.join(right))