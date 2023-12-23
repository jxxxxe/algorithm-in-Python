from collections import deque

M, N, H = map(int, input().split())
tomatos = [[[t for t in map(int, input().split())] for _ in range(N)] for _ in range(H)]
                
def exist_unripe():
    for z in range(H):
        for i in range(N):
            for j in range(M):
                if tomatos[z][i][j] == 0:
                    return True
    return False

def is_unripe(z,i,j):
    if 0<=z<H and 0<=i<N and 0<=j<M and tomatos[z][i][j]==0:
        tomatos[z][i][j] = 2
        queue.append([z,i,j])


if not exist_unripe():
    print(0)
    exit()

queue = deque()
count = -1

for z in range(H):
    for i in range(N):
        for j in range(M):
            if tomatos[z][i][j] == 1:
                queue.append([z,i,j])

while queue:
    for _ in range(len(queue)):
        cz,ci,cj = queue.popleft()
        is_unripe(cz-1,ci,cj)
        is_unripe(cz+1,ci,cj)
        is_unripe(cz,ci-1,cj)
        is_unripe(cz,ci+1,cj)
        is_unripe(cz,ci,cj-1)
        is_unripe(cz,ci,cj+1)
    count+=1
                
print(count if not exist_unripe() else -1)