#블랙잭
def blackjack(n,m,list):
    min=0
    for one in range(0,n-2):
        for two in range(one+1,n-1):
            for three in range(two+1, n):
                sum=list[one]+list[two]+list[three]
                if sum<=m:
                    if min<sum:
                        min=sum
    return min

N,M=input().split()
list=input().split()

list=[int(i) for i in list]

print(blackjack(int(N),int(M),list))