#이진 탐색으로 풀어야 시간초과가 나지 않는다.
#원래 내 풀이) 제일 긴 전선을 등분한 것을 기준으로 길이를 찾는다.
#제일 작은 길이의 전선보다 더 크게 잘라서 갯수를 채울 수 있다면?
K,N=map(int,input().split())
list=[]

for _ in range(K):
    list.append(int(input()))

list.sort()
list.reverse()

if N==1:
    print(list[0])
    exit()

for j in range(1,list[0]+1):
    minlen=list[0]//j
    count=0
    for i in range(K):
        count+=list[i]//minlen
    if count>=N:
        maxlen=list[0]//(j-1)
        break

for len in range(minlen,maxlen+1):
    count=0
    for i in range(K):
        count+=list[i]//len
    if count<N:
        print(len-1)
        break