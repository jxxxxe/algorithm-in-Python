#https://www.acmicpc.net/problem/11723
#set() / set(리스트) 
#그냥 스택으로 풀면 안된다..<비트마스킹>을 사용하자
#비트마스킹 : 불리언 값으로 이루어진 집합에 대해서 빠르게 연산하는 기법, 정수를 이진수로 표현
#완전탐색의 속도를 빠르게 하기 위해 쓰이기도 하고 DP이 가능함
'''         <<<<비트 연산의 응용>>>>
i번째 원소 추가       S |= (1 << i)
i번째 원소 제거       S &= ~(1 << i)
i번째 원소 조회       if(S & (1 << i))  =>1이상이면 있고, 0이면 없는 것
i번째 상태 변환       S ^= (1 << i)
n크기 집합 모두 1로 변환     (1 << n) - 1

*S는 0으로 초기화 한다.
'''
#또!!또!! 이봐!! 나 또 무시하잖아!! 이론씨 대체 왜그래 나한테 정말!!!
#ㄱ-.. 파이썬은 이론처럼 되기는 하는데 걍 편하게 드가자~
import sys

N=int(input())

jibhab=[0]*20
for _ in range(N):
    line=sys.stdin.readline().strip().split()
    if len(line)==1:    operator=line[0]
    else:    operator,x=line[0],int(line[1])-1

    if operator=='add':
        jibhab[x]=1
    elif operator=='remove':
        jibhab[x]=0
    elif operator=='check':
        print(jibhab[x])
    elif operator=='toggle':
        jibhab[x]=1-jibhab[x]       ####
    elif operator=='all':
        jibhab=[1]*20
    elif operator=='empty':
        jibhab=[0]*20