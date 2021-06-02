import sys
N,M,B=map(int,input().split())

ground=[]
for _ in range(N):
    line=list(map(int,sys.stdin.readline().split()))
    for l in line:
        ground.append(l)

max_h=max(ground)
min_h=min(ground)

time=[]
for pivot in range(min_h,max_h+1):
    count,error=0,0
    for g in ground:
        if g<=pivot:
            count+=pivot-g
            B-=pivot-g
            if B<0:
                error=1
                break
        else:
            count+=2*(g-pivot)
    if not error:
        time.append(count,pivot)

min=max_h*N*M
for i,t in enumerate(time):
    if min>=t:
        min=t
        h=i+min_h

print(min,h)