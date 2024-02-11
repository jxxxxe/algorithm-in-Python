#덩치
#키, 몸무게 둘 중 하나라도 같으면 비교 불가!! 문제를 제대로 읽자^^;

N=int(input())

w=[]
h=[]
rank=[]
for _ in range(N):
    weight,height=map(int,input().split())
    w.append(weight)
    h.append(height)
    rank.append(1)

for i in range(N):
    for j in range(N):
        if w[i]<w[j] and h[i]<h[j]:
            rank[i]+=1

for i in rank:
    print(i,end=' ')