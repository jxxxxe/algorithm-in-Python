N,K=input().split()
N=int(N)
K=int(K)
result=1
count=0

for i in range(1,N+1):
    result*=i
for j in range(1,K+1):
    result//=j
for k in range(1,N-K+1):
    result//=k

while(result%10==0):
    count+=1
    result//=10

print(count)