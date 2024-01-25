from collections import deque

N, K = map(int, input().split())
nums = list(map(int,input().split()))

idx_dic={}
result = 0
start=0

for i,num in enumerate(nums):
    if num not in idx_dic:
        idx_dic[num] = deque([])

    idx_dic[num].append(i)

    if len(idx_dic[num]) == K+1:
        result = max(result, i-start)
        for prev_idx in range(start,idx_dic[num][0]):
            prev_num = nums[prev_idx]
            idx_dic[prev_num].popleft()
        start = idx_dic[num][0]+1
        idx_dic[num].popleft()
else:
    result = max(result, N-start)


print(result)