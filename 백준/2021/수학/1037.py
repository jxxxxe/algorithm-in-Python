N=int(input())
list=list(map(int,input().split()))

max=list[0]
min=list[0]
for i in list:
    if i>max:
        max=i
    if i<min:
        min=i

print(min*max)
