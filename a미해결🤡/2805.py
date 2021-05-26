N,M=map(int,input().split())
tree=[]
tree=list(map(int,input().split()))
#N: 나무개수, M: 가져갈 길이
tree.sort()
tree.reverse()
{key:1,1}
h=0
count=1
rest=M
while h<M:
    tree[0]-M
    for i in range(count):
        h+=list[i]-list[count] #그 다음으로 작은 나무에 맞춰 자르고 난 후
    if h<M:
        count+=1
        for i in range(count):
            list[i]-=list[count]
    rest-=h