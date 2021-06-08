import sys

max=123456
prime=[0]*(2*max+1)
prime[0],prime[1]=1,1
for num in range(2,int((2*max)**0.5+1)):
    if prime[num]==0:
        for i in range(num*2,2*max+1,num):
            prime[i]=1

while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    print(prime[n+1:2*n+1].count(0))