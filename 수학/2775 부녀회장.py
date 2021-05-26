#쉬운 구현을 생각했는데도 시간 초과 될까봐 다른 방법을 찾아 며칠간 고뇌했던 썰 푼다.txt
import sys

T=int(input())
for _ in range(T):
    k=int(sys.stdin.readline().strip()) #층
    n=int(sys.stdin.readline().strip()) #호

    #호는 0~n-1호로 변경
    people=[[0 for ho in range(n)] for floor in range(k+1)]
    for f in range(k+1):
        for h in range(n):
                if f==0:
                    people[f][h]=h+1    #0층일 때
                else:
                    for i in range(h+1):    #0~h호까지
                        people[f][h]+=people[f-1][i] #밑층의 0~h호의 합
    print(people[k][n-1])