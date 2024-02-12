n=int(input())
nums = list(map(int,input().split()))

dp=[[num] for num in nums]
for i in range(1,len(nums)):
    for j in range(i):
        if dp[j][-1]<nums[i] and len(dp[j])>=len(dp[i]):
            dp[i]=dp[j]+[nums[i]]

result=max(dp,key=len)
print(len(result))
print(' '.join(map(str,result)))