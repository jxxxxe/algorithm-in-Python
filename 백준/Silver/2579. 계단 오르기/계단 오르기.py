import sys

input=sys.stdin.readline

n=int(input())
steps=[0]

[steps.append(int(input())) for _ in range(n)]
dp=[0 for _ in range(n+1)]

if n==1:
    print(steps[1])
    exit()

dp[1], dp[2] = steps[1], steps[1]+steps[2]

for i in range(3,n+1):
    dp[i]=max(dp[i-2],steps[i-1]+dp[i-3])+steps[i]

print(dp[n])