n,m=map(int,input().split())

if n-m<m:
    m=n-m

result=1
for i in range(n,n-m,-1):
    result*=i

for j in range(m,0,-1):
    result/=j

print(str(result)[::-1])