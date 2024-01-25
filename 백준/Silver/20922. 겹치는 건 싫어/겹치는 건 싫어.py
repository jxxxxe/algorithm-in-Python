from collections import deque

N, K = map(int, input().split())
nums = list(map(int,input().split()))

counter={}
result = 0
start=0

for i,num in enumerate(nums):
    if num not in counter:
        counter[num] = 0

    counter[num]+=1

    while counter[num]>K:
        prev_num = nums[start]
        counter[prev_num]-=1
        start+=1

    result = max(result, i-start+1)

print(max(result, N-start))