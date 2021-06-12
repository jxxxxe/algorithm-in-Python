def fibo(n):
    F,order=[0,1],0
    for _ in range(2,n):
        F[order]=sum(F)%1000000007
        print(F[order])
        order=1 if order==0 else 0
    return sum(F)%1000000007

print(fibo(1000000000))