N=int(input())
list=[]

for i in range(0,N):
    M=int(input())
    list.append(M)
    for j in list:
        if j>=M:
            index=list.index(j)
            list.insert(index,list.pop())
            break

for k in list:
    print(str(k))

#삽입정렬


