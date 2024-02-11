#https://www.acmicpc.net/problem/11497
#deque선언시 원소를 넣을 땐 deque([대괄호필수])
#차이는 abs 빼먹지 않게 주의
#처음과 마지막을 비교를 안했었다 엣콩!
import sys
from collections import deque

T=int(input())

for _ in range(T):
    N=int(sys.stdin.readline())
    trees=list(map(int,sys.stdin.readline().split()))

    trees.sort()
    min=trees[0]
    trees=list(i-min for i in trees)

    tree_updown=deque([trees.pop()])

    while len(trees)>0:
        tree_updown.append(trees.pop())
        if len(trees)>0:
            tree_updown.appendleft(trees.pop())

    max=0
    for i in range(N-1):
        if max<abs(tree_updown[i+1]-tree_updown[i]):
            max=abs(tree_updown[i+1]-tree_updown[i])

    if max<abs(tree_updown[len(trees)-1]-tree_updown[0]):
        max=abs(tree_updown[i+1]-tree_updown[i])

    print(max)