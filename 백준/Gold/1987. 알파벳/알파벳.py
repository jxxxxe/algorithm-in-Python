import sys

input=sys.stdin.readline

r,c = map(int,input().split())
graph=[list(input().strip()) for _ in range(r)]

pos=[-1,1]
answer=set()

def dfs(i,j,visited):
    for p in pos:
        if 0<=j+p<c and graph[i][j+p] not in visited:
            visited.add(graph[i][j+p])
            dfs(i,j+p,visited)
            visited.remove(graph[i][j+p])
        if 0<=i+p<r and graph[i+p][j] not in visited:
            visited.add(graph[i+p][j])
            dfs(i+p,j,visited)
            visited.remove(graph[i+p][j])
    answer.add(len(visited))

dfs(0,0,set([graph[0][0]]))
print(max(answer))