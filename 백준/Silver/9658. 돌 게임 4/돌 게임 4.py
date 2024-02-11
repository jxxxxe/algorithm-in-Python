n=int(input())
dp = [0,0,1,0]+[0]*(n-3)

for i in range(4,n+1):
    if not dp[i-1] or not dp[i-3] or not dp[i-4]:
        dp[i]=1

print("SK" if dp[n] else "CY")