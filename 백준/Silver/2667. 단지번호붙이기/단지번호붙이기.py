N = int(input())
map=[[int(i) for i in input()] for _ in range(N)]
counts=[]

def dfs(a,b,idx):
    if a<0 or b<0 or a>=N or b>=N or map[a][b] != 1:
        return
    map[a][b] = 2
    counts[idx]+=1
    dfs(a,b+1,idx)
    dfs(a+1,b,idx)
    dfs(a-1,b,idx)
    dfs(a,b-1,idx)
    

for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            counts.append(0)
            dfs(i, j,len(counts)-1)

print(len(counts))
print(("\n").join([str(count) for count in sorted(counts)]))