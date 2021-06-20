import sys

T=int(input())

for _ in range(T):
    N=int(sys.stdin.readline())
    values=list(map(int,sys.stdin.readline().split()))
    max_idx,max,total,tmp_sum=len(values)-1,values[-1],0,0
    
    for i in range(len(values)-2,-1,-1):
        if values[i]>max or (i==0 and values[0]<max):
            if i==0 and values[0]<=max:
                i-=1
                tmp_sum+=values[0]
            total+=max*(max_idx-i-1)-tmp_sum
            max_idx,max=i,values[i]
            tmp_sum=0
        else:
            tmp_sum+=values[i]
    
    print(total)