import sys

def get_primary(max):
    primary=[1]*(max+1)
    primary[0],primary[1]=0,0
    for i in range(2,int((max+1)**0.5)+1):
        if primary[i]!=0:
            for j in range(i*2,max+1,i):
                primary[j]=0
    real_primary=[]
    for index,p in enumerate(primary):
        if p>0:
            real_primary.append(index)
    return real_primary

T=int(input())
for _ in range(T):
    n=int(sys.stdin.readline())
    primary=get_primary(n)
    left,right=0,len(primary)-1
    while left<=right:
        result=primary[left]+primary[right]
        if result==n:
            a,b=primary[left],primary[right]
        if result<=n:
            left+=1
        if result>=n:
            right-=1

    print(a,b)