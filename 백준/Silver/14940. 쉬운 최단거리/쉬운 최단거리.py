import sys
from collections import deque

row_num, col_num = map(int, input().split())
dest = [0,0]
jido = []
is_visit_jido = [[False for _ in range(col_num)] for _ in range(row_num)]

#지도 입력 받기
for i in range(row_num):
    line = list(map(int,sys.stdin.readline().split()))

    if 2 in line:
        dest_idx = line.index(2)
        dest = [i, dest_idx]
        line[dest_idx] = 0
    jido.append(line)


def is_land(row, col, prev_val):
    if 0<=row<row_num and 0<=col<col_num and not is_visit_jido[row][col] and jido[row][col] == 1:
        jido[row][col] = prev_val+1
        is_visit_jido[row][col] = True
        return True
    return False

#bfs
queue = deque([dest])
while queue:
    cur = queue.popleft()
    cur_r, cur_c = cur[0], cur[1]
    cur_val = jido[cur_r][cur_c]

    if is_land(cur_r+1, cur_c, cur_val):
        queue.append([cur_r+1, cur_c])

    if is_land(cur_r, cur_c+1, cur_val):
        queue.append([cur_r, cur_c+1])

    if is_land(cur_r-1, cur_c, cur_val):
        queue.append([cur_r-1, cur_c])

    if is_land(cur_r, cur_c-1, cur_val):
        queue.append([cur_r, cur_c-1])

for i in range(row_num):
    col_result = []
    for j in range(col_num):
        col_result.append(-1 if jido[i][j] == 1 and not is_visit_jido[i][j] else jido[i][j])

    print(*col_result)
     