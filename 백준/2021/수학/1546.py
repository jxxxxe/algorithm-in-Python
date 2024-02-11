#새로운 평균

N=int(input())
list=list(map(int,input().split()))
sum=0
M=max(list)

for i in list:
    sum+=i

new=sum*100/M/N