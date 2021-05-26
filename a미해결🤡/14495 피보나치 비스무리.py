def fibo_similar(n):
    if n==1 or n==2 or n==3:
        return 1
    else:
        return fibo_similar(n-1)+fibo_similar(n-3)

N=int(input())

print(fibo_similar(N))