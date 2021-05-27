import sys

N=int(sys.stdin.readline().strip())
M=int(sys.stdin.readline().strip())
IOIs=sys.stdin.readline().strip()

length=N+N-1+2
start,count=0,0
for i in range(1,M):
    if IOIs[i-1]==IOIs[i]:
        if i-start>=length:
            if IOIs[start]=='O':
                start+=1
            if IOIs[i-1]=='O':
                i-=1
            count+=i-start-length+1
            print(start,i,count)
        start=i

print(count)