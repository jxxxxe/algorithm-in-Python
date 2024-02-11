#에라토스테네스의 체로 푸는 소수 구하기~!!~!
#제곱근까지만 구해도 되는 이유 : 
M,N=map(int,input().split())

prime=list(range(N+1))

for i in range(2,int((N+1)**0.5+1)):
    j=2
    while prime[i]!=0 and i*j<=N:
        prime[i*j]=0
        j+=1

for i in range(M,N+1):
    if i>1 and prime[i]!=0:
        print(prime[i])