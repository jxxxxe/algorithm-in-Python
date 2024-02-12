import sys

input=sys.stdin.readline

n=int(input())

steps=[0]*301
dp=[0]*301

for i in range(1,n+1):
    steps[i]=int(input())

dp[1], dp[2] = steps[1], steps[1]+steps[2]

for i in range(3,n+1):
    dp[i]=max(dp[i-2],steps[i-1]+dp[i-3])+steps[i]

print(dp[n])