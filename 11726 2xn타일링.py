def coper(n,r):
    if n-r<r:
        r=n-r
    return facto(n)//(facto(r)*facto(n-r))

def facto(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

n=int(input())
count=0
for i in range(n//2+1):
    count+=coper(n-i,i)

print(count%10007)