N,K=input().split()
N=int(N)
K=int(K)

list=[]
count=0

for i in range(N):
    list.insert(0,int(input()))

for j in list:
    count+=K//j
    K%=j

print(count)