def facto(n):
    if n<=1:
        return 1
    else:
        return n*facto(n-1)

N=int(input())
print(facto(N))