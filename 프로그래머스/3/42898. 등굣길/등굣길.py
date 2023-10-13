def is_puddle(x,y,puddles):
    for px,py in puddles:
        if x == px and y == py:
            return True
        
    return False

def solution(m, n, puddles):
    dp = [[0]*(n+1)]*(m+1)
    dp[1][1]=1
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i==1 and j==1:
                continue
            if is_puddle(i,j,puddles):
                dp[i][j]=0
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m][n]% 1000000007