N=int(input())
list=[]

for i in range(N):
    M=int(input())
    list.append(M)

list.sort()
for k in list:
    print(str(k))