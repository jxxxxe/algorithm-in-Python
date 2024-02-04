n,k = map(int,input().split())

def dfs(cur):
    if cur==n:
        return 0
    if cur==1:
        return 1
    if cur<n:
        return n-cur
    if cur%2:
        return 1+min(dfs(cur-1),dfs(cur+1))
    return min(cur-n,dfs(cur//2))

if n>=k:
    print(n-k)
else:
    print(dfs(k))