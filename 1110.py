N=int(input())

new_num=str(N)
count=0
while True:
    total=0
    for n in new_num:
        total+=int(n)
    new_num=new_num[-1]+str(total)[-1]
    count+=1

    if N==int(new_num):
        break

print(count)