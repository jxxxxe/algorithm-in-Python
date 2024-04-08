import sys

change_list = [[] for _ in range(10)]

change_list[0]=[0,4,3,3,4,3,2,3,1,2]

def reverse_input(i):
    for j in range(i):
        change_list[i].append(change_list[j][i])
    change_list[i].append(0)

reverse_input(1)
change_list[1].extend([5,3,2,5,6,1,5,4])
reverse_input(2)
change_list[2].extend([2,5,4,3,4,2,3])
reverse_input(3)
change_list[3].extend([3,2,3,2,2,1])
reverse_input(4)
change_list[4].extend([3,4,3,3,2])
reverse_input(5)
change_list[5].extend([1,4,2,1])
reverse_input(6)
change_list[6].extend([5,1,2])
reverse_input(7)
change_list[7].extend([4,3])
reverse_input(8)
change_list[8].extend([1])
reverse_input(9)

input = sys.stdin.readline

max_val, jari, max_change, cur_val = map(int,input().split())

def append_zero(num):
    num_jari=len(str(num))
    num_list=[0]*(jari-num_jari)+list(map(int,list((str(num)))))
    return num_list

cur_list = append_zero(cur_val)

result=0
for i in range(1,max_val+1):
    if i==cur_val:
        continue

    i_list = append_zero(i)
    change_count=0

    for j in range(jari):
        cur,target=i_list[j], cur_list[j]
        change_count+=change_list[cur][target]
    if change_count<=max_change:
        result+=1

print(result)