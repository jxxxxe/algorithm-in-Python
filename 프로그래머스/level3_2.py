from collections import defaultdict
def solution(n, costs):
    answer = 0
    graph=defaultdict(dict)
    for c in costs:
        graph[c[0]][c[1]],graph[c[1]][c[0]]=c[2],c[2]
    print(min(graph[2].values()))
    
    return graph

print(solution(5,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))