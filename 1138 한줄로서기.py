#https://www.acmicpc.net/problem/1138
#입력으로 주어진 리스트를 차례로 돈다. 해당 인덱스 값은 남은 여석 내에 순서를 의미한다. 차례차례로 좌석을 채워주면 됐던 문제.
#채워진 자리를 어떻게 배제하는게 효율적일까 고민을 많이 했던 문제
#내 방법) 자리표 리스트를 만들어서 채워진 자리는 그 리스트에서 빼버린 식으로 했다.
#다른 방법) for문을 돌면서 채워진 자리라면 카운트 안하고 넘어가는 식으로 해서 자리 찾는 방법 >>시간이 많이 걸릴 줄 알고 처다도(?) 안봤는데 의외로 시간이 적게 걸리는거 같음

N=int(input())
people=list(map(int,input().split()))
line=list(i for i in range(N))
final={}

for i,p in enumerate(people):
    final[line[p]]=i+1
    del line[p]

for p in sorted(final.items()):
    print(p[1],end=' ')