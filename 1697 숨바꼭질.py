def move(n,k):
    X=set([n])
    i=0
    while k not in X:
        tmp=set()
        for x in X:
            if x-1>=0:
                tmp.add(x-1)
            tmp.add(x+1)
            tmp.add(2*x)
        X=tmp
        i+=1
    return len(X)

N,K=map(int,input().split())
print(move(N,K))