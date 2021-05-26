N=int(input())
list=[]
while N>0:
    list.append(N%10)
    N//=10
list=sorted(list,key=lambda x:-x)

for l in list:
    print(l,end='')