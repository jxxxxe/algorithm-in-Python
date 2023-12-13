total_leng, wanted_leng = map(int, input().split())
visits = list(map(int, input().split()))

if sum(visits)==0:
    print("SAD")
    exit()

cur_sum = sum(visits[:wanted_leng])
max_sum=cur_sum
max_count=1

for i in range(wanted_leng, total_leng):
    cur_sum+=visits[i]
    cur_sum-=visits[i-wanted_leng]
    if max_sum<cur_sum:
        max_sum, max_count = cur_sum, 1
    elif max_sum==cur_sum:
        max_count+=1

print(max_sum)
print(max_count)