import sys

T=int(input())

for _ in range(T):
    N=int(sys.stdin.readline())
    values=list(map(int,sys.stdin.readline().split()))
    total,index=0,0

    for i,max in sorted(enumerate(values),key=lambda x:-x[1]):
        if index<i:
            total+=max*(i-index)-sum(values[index:i])
        index=i+1
        
        if i>=N-2:
            break
    
    print(total)