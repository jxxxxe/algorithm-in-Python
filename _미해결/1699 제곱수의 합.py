N=int(input())

count=0
while int(N**0.5)>=2:
    count+=1
    x=int(N**0.5)
    N-=x**2

count+=N

print(count)