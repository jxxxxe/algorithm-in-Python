def factorial(a):
    result=1
    for i in range(a):
        result*=i+1
    return result

n,m=map(int,input().split())

if n-m<m:
    m=n-m

result=str(factorial(n)//(factorial(m)*factorial(n-m)))

for i in range(1,len(result)+1):
    if result[-i]!='0':
        print(i-1)