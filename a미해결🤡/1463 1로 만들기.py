N=int(input())

count=0
while N%3==0 or N%2==0:
    N-=1
    count+=1

