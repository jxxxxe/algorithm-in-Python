N=int(input())
pair_count=int(input())
graph=[set() for _ in range(N)]
answer=set([0])

for _ in range(pair_count):
    a, b = map(int, input().split())
    graph[a-1].add(b-1)
    graph[b-1].add(a-1)

def dfs(idx):
    for computer in graph[idx]:
        if computer not in answer:
            answer.add(computer)
            dfs(computer)

dfs(0)
print(len(answer)-1)