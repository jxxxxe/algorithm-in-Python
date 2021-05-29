N=int(input())

N,k=map(int,input().split())

max_length=0
for i in range(1,len(str(N))):
    max_length+=i*(9*10**i)

max_length+=len(str(N))*(N-10**(str(N)-1))

if k<max_length:
    print(-1)
else:
    