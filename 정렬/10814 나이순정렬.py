import sys

N=int(input())
list=[]

for _ in range(N):
    age,name=sys.stdin.readline().split()
    list.append((int(age),name))

sort=sorted(list, key=lambda x:x[0])
for s in sort:
    print(str(s[0])+" "+s[1])


#버블정렬 => 시간 초과
#사전 => 동명(+동나이) 이인을 처리하지 못하고 갱신해버림 => 튜플로 변경
#튜플로 입력받을 때 한 변수로 받으면 정수를 처리 못함 주의