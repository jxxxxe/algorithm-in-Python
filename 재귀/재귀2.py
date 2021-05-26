def fibo(n,i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return fibo(n,i-1)+fibo(n,i-2)

N=int(input())
print(fibo(N,N))