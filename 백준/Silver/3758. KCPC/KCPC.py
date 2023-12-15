import sys

T=int(sys.stdin.readline().strip())

for _ in range(T):
    team_count, q_count, my_id, m = map(int, sys.stdin.readline().split())
    teams_info = [{ "score": [0 for _ in range(q_count)], "count":0, "last_idx":m-1} for _ in range(team_count)]

    for idx in range(m):
        id, q_num, score = map(int, sys.stdin.readline().split())
        teams_info[id-1]["count"]+=1
        teams_info[id-1]["score"][q_num-1] = max(teams_info[id-1]["score"][q_num-1], score)
        teams_info[id-1]["last_idx"] = idx
    sorted_teams=sorted(range(len(teams_info)), key= lambda idx: (-sum(teams_info[idx]["score"]), teams_info[idx]["count"], teams_info[idx]["last_idx"]))
    print(sorted_teams.index(my_id-1)+1)