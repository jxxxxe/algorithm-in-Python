#for i in range(N,-1,-1): 0~N부터 역순으로
#for i in range(N)~ if:break : break가 되지 않고 끝까지 간다해도 i=N-1까지만 감.
#a==1일때 j처리 주의!
import sys

a=int(input())
b=int(input())

list=[]
j=2
for i in range(a,b+1):
    for j in range(2,i+1):
        if i%j==0:
            break
    if j==i:
        list.append(i)

if list==[]:
    print("-1")
    exit()
print(sum(list))
print(list[0])

''' 처음 풀었던 방법
M=int(input())
N=int(input())

min=0
sum=0
for i in range(M,N+1):
    j=2
    while j<i:
        if i%j==0:
            break
        j+=1
        
    if j==i:
        if sum==0:
            min=i
        sum+=i

if sum==0:
    print("-1")
else:
    print(sum)
    print(min)
'''