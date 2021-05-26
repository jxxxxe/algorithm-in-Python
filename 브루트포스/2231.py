#분해합
def boonhae(n):
    for i in range(0,n):
        sum=i
        num=i
        while num!=0:
            sum+=num%10
            num//=10
        if sum==n:
            return i
    return 0


N=int(input())
print(boonhae(N))