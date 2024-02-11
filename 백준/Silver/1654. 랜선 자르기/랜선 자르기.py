K,N=map(int,input().split())
list=[]

for _ in range(K):
    list.append(int(input()))

left,right=1,max(list)
while left<=right:
    center,sum=(left+right)//2,0
    for l in list:
        sum+=l//center
    if sum>=N:
        left=center+1
    else:
        right=center-1

print(right)