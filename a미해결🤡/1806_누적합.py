N,S=map(int,input().split())

num=list(10000 for _ in range(100000))

accum,sum=[],0
for n in num:
    sum+=n
    accum.append(sum)

length=0
for L in range(1,N+1):
    for j in range(N-L+1):
        sum=accum[j+L-1]-accum[j-1] if j>0 else accum[j+L-1]
        if sum>=S:
            print(L)
            exit()

print(0)