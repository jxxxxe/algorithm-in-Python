import sys

input=sys.stdin.readline

n=int(input())
nums=list(map(int,input().split()))
nums.sort()
answer=[0]*n

for i in range(n):
    left, right = 0,n-1
    while left<right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -=1
            continue

        result=nums[left]+nums[right]
        if result==nums[i]:
            answer[i]=1
            break
        elif result<nums[i]:
            left+=1
        elif result>nums[i]:
            right-=1

print(sum(answer))