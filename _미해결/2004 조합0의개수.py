def factorial(a,count):
    result,end=1,a-count
    for i in range(a,end,-1):
        result*=i
    return result

n,m=map(int,input().split())

if n-m<m:
    m=n-m

result=str(factorial(n,m)//factorial(m,m))

for i in range(1,len(result)+1):
    if result[-i]!='0':
        print(i-1)
        break