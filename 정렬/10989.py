#사전방식, 삽입정렬 => 시간초과
#수의 범위가 적으니까 사전방식+@인 카운팅 정렬로 조사버리자
#for(n,0,-1) => n~1까지

import sys
from collections import Counter

N=int(input())
arr=[]

for i in range(N):
    arr.append(int(sys.stdin.readline().strip()))

for n,count in sorted(Counter(arr).items(),key=lambda x:x[0]):
    for i in range(count):
        print(n)