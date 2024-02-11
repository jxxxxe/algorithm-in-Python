#사전방식, 삽입정렬 => 시간초과
#수의 범위가 적으니까 사전방식+@인 카운팅 정렬로 조사버리자 =>?
#카운팅 정렬:항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여 선형 시간에 정렬하는 알고리즘
#보통 카운팅 정렬처럼 풀면 메모리 초과난다. 
# 자꾸 메모리 초과가 나서 모범 답안 참고 함. 
# 리스트 하나로도 풀 수 있는데 걍 카운팅 정렬에서 카운트하는 것만 같음.. 카운팅정렬아니네;
#for(n,0,-1) => n~1까지

import sys

N=int(input())
count=[0 for _ in range(10000+1)]
for i in range(N):
    count[int(sys.stdin.readline())]+=1

for num,many in enumerate(count):
    for _ in range(many):
        print(num)