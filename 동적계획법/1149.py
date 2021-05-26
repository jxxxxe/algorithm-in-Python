N=int(input())
list=[][]
sum=0
min=0

for i in range(N):
    list[i][0],list[i][1],list[i][2]=input().split


    for j in range(1:N):
        for k in range(3):
            if j==0:
                min=findmin(list[0],-10)
                precolor=list[0].index(min)
                sum+=min


def findmin(list[],precolor):
    for i in list:
        list[i]<list[i+1]
        


