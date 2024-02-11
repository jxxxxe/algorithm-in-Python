N=int(input())
list=[]
M=N

while M!=0:
    list.append(M%10)
    for j in list:
        if j>=M%10:
            index=list.index(j)
            list.insert(index,list.pop())
            break
    M//=10

for k in list:
    print(str(k))