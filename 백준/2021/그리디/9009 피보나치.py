import sys
T=int(input())

fibo,i=[0,1],2
while True:
    fi=fibo[i-1]+fibo[i-2]
    if fi>1000000000:
        break
    fibo.append(fi)
    i+=1

for _ in range(T):
    n=int(sys.stdin.readline())
    prr=[]
    for f in fibo[::-1]:
        if f<=n:
            prr.append(str(f))
            n-=f
        if n==0:
            break
    print(' '.join(prr[::-1]))