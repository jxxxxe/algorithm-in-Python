#파이썬에서 큐를 다루는 방법(방법1, 2 모두 데이터 추가/삭제는 O(1), 접근은O(n))

#방법1은 collections 모듈의 deque 클래스를 import 한 후 deque([list])를 이용해 조작=> from collections import deque
#방법1. queue.append(i), popleft()     /   반대방향으로(맨앞삽입,맨뒤추출) : appendleft(i), pop()
#queue를 출력하면 deque=[] 형태임

#방법2는 from queue import Queue 한 후 Queue()를 이용해 조작
#방법2. que.put(i), que.get() (Queue클래스 사용하기)
#각 인덱스를 참조 못하는듯..; 얘는 queue출력하면 이상하게 나옴;

#(cf. list를 이용해서 append,pop(0),insert(0,x)을 사용하는 방법도 있겠지만, 
#                                               이 방법은 pop후 뒤의 원소들을 앞으로 당겨와야 하므로 성능 bad. 삭제O(n))
from collections import deque
import sys

N=int(input())
queue=deque()

for _ in range(N):
    line=sys.stdin.readline().strip()
    if line[:4]=='push':
        queue.append((line[5:]))
    elif (line=='pop' or line=='front' or line=='back') and queue==deque([]):
        print(-1)
    elif line=='pop':
        print(queue.popleft())
    elif line=='size':
        print(len(queue))
    elif line=='empty':
        print(int(queue==deque([])))
    elif line=='front':
        print(queue[0])
    elif line=='back':
        print(queue[-1])

#push x를 대응하기 위해 readline().split()으로 명령을 입력 받으면 push는 line[0], x는 line[1]로 접근 가능