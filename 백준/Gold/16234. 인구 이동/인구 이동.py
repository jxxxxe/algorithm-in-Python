import sys

input = sys.stdin.readline

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
li = [[i, j] for j in range(N) for i in range(N)]
visited = [[0] * N for _ in range(N)]
day = 1

while 1:
    for _ in range(len(li)):
        i, j = li.pop(0)
        if visited[i][j] == day:
            continue

        queue = [[i, j]]
        total = A[i][j]
        cnt = 1
        pos_list = [[i, j]]
        visited[i][j] = day

        while queue:
            i, j = queue.pop()
            for dy, dx in delta:
                if N > i+dy >= 0 and N > j+dx >= 0:
                    if visited[i+dy][j+dx] != day:
                        if R >= abs(A[i+dy][j+dx]-A[i][j]) >= L:
                            total += A[i+dy][j+dx]
                            cnt += 1
                            visited[i+dy][j+dx] = day
                            pos_list.append([i+dy, j+dx])
                            queue.append([i+dy, j+dx])
        if len(pos_list) > 1:
            n = total // cnt
            while pos_list:
                i, j = pos_list.pop()
                A[i][j] = n
                li.append([i, j])

    if li:
        day += 1
    else:
        break

print(day-1)