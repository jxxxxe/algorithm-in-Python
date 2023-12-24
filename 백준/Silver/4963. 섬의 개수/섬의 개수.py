import sys

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w==0 and h==0:
        break

    maps=[]
    land_xy=[]
    for i in range(h):
        line = list(map(int,sys.stdin.readline().split()))
        maps.append(line)
        for j in range(w):
            if line[j]==1:
                land_xy.append([i,j])
    
    def is_land(i,j):
        if 0<=i<h and 0<=j<w and maps[i][j] == 1:
            return True
        return False
    
    def dfs(i,j):
        stack=[]
        stack.append([i,j])
        while stack:
            [x,y] = stack.pop()
            if not is_land(x,y):
                continue
            maps[x][y]=2
            stack.append([x+1,y])
            stack.append([x,y+1])
            stack.append([x-1,y])
            stack.append([x,y-1])
            stack.append([x+1,y+1])
            stack.append([x+1,y-1])
            stack.append([x-1,y+1])
            stack.append([x-1,y-1])

    count=0
    while land_xy:
        x, y = land_xy.pop()
        if maps[x][y] == 1:
            count+=1
            dfs(x, y)
    
    print(count)