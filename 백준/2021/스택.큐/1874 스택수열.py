import sys
N=int(input())

nums=[]
stack=[]
op=[]
max=1
for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))

for i in range(N):
    if i==0 or nums[i]>nums[i-1]:
        if nums[i]<max:
            print("NO")
            exit()
        while nums[i]>=max:
            stack.append(max)
            op.append("+")
            max+=1
    while stack!=[] and stack[-1]!=nums[i]:
        if stack[-1]<nums[i]:
            print("NO")
            exit()
        stack.pop()
        op.append("-")
    stack.pop()
    op.append("-")

for o in op:
    print(o)