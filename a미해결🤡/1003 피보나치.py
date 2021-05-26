import sys

def fibo(N):
    # global count0
    # global count1

    if N==0:
        list[0]+=1
    elif N==1:
        list[1]+=1
    else:
        fibo(N-1)
        fibo(N-2)

T=int(input())

for _ in range(T):
    n=int(sys.stdin.readline().strip())
    # count0=0
    # count1=0
    list=[0,0]
    fibo(n)
    # print("%s %s"%(count0,count1))
    print("%s %s"%(list[0],list[1]))