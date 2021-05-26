#ATM
N=int(input())

list=list(map(int,input().split()))

for i in range(N-1):
    min=list[i]
    for j in range(i+1,N):  #선택정렬, j의 범위, 최소값갱신, 값바꾸기 실수하지 말기!
        if min>list[j]:
            tmp=min
            list[i]=list[j]
            min=list[j]
            list[j]=tmp

wait=0
sum=0
for i in range(N):
    wait+=list[i]
    sum+=wait

print(sum)