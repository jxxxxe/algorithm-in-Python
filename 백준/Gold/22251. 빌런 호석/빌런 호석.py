import sys

change_list = [[] for _ in range(10)]

change_list=[[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]

input = sys.stdin.readline

max_val, jari, max_change, cur_val = map(int,input().split())

cur_str = str(cur_val).zfill(jari)

result=0
for i in range(1,max_val+1):
    if i==cur_val:
        continue

    i_str = str(i).zfill(jari)
    change_count=0
    for j in range(jari):
        for i_jari, c_jari in zip(change_list[int(i_str[j])],change_list[int(cur_str[j])]):
            if i_jari != c_jari:
                change_count+=1
    
    if change_count<=max_change:
        result+=1

print(result)