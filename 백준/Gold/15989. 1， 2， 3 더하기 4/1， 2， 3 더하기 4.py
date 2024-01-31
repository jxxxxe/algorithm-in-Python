import sys

input = sys.stdin.readline
T = int(input())
nums = []
for _ in range(T):
    nums.append(int(input()))

max=max(nums)

dp=[1]*(max+1)

for i in range(2,max+1):
    dp[i]+=dp[i-2]

for i in range(3,max+1):
    dp[i]+=dp[i-3]

for num in nums:
    print(dp[num])