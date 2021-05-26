N=int(input())
dist=list(map(int,input().split()))
cost=list(map(int,input().split()))

cost=cost[:N-1]
min=cost[0]
sum=0
for i in range(N-1):
    if min>cost[i]:
        sum+=cost[i]*dist[i]
        min=cost[i]
    else:
        sum+=min*dist[i]

print(sum)


# min()을 사용하면 시간 초과!!!(아쉽~)
# endindex=len(cost)
# sum=0
# while True:
#     index=cost.index(min(cost))
#     for j in range(index,endindex):
#         sum+=cost[index]*dist[j]
#     if index==0:
#         break
#     endindex=index
#     cost=cost[:index]

# print(sum)