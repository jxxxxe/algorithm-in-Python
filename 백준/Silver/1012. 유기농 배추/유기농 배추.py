import sys

T = int(sys.stdin.readline())

def is_baechoo(i,j):
    if 0<=i<N and 0<=j<M and graph[i][j]==1:
        return True
    return False

for _ in range(T):
    M,N,K = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x,y = map(int,sys.stdin.readline().split())
        graph[y][x]=1
    queue=[]
    count=0
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1:
                queue.append([i,j])
                while queue:
                    [cur_i, cur_j] = queue.pop()
                    graph[cur_i][cur_j]=2
                    if is_baechoo(cur_i+1,cur_j):
                        queue.append([cur_i+1,cur_j])
                    if is_baechoo(cur_i-1,cur_j):
                        queue.append([cur_i-1,cur_j])
                    if is_baechoo(cur_i,cur_j+1):
                        queue.append([cur_i,cur_j+1])
                    if is_baechoo(cur_i,cur_j-1):
                        queue.append([cur_i,cur_j-1])
                count+=1
    print(count)