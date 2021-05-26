import sys
T=int(input())

for _ in range(T):
    nums=list(map(int,sys.stdin.readline().split()))
    n=nums[0]
    nums=nums[1:]
    total=0
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            a,b=nums[i],nums[j]
            while b>0:
                if a<b:
                    a,b=b,a
                a,b=b,a%b
            total+=a
    print(total)