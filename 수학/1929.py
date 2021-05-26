#에라토스테네스의 체로 푸는 소수 구하기~!!~!

M,N=map(int,input().split())

endnum=int(N**0.5)
list=[]

for i in range(2,endnum+1):
    j=i
    while (not i in list) and i*j<=N:
        list.append(i*j)
        j+=1

for i in range(M,N):
    if not i in list:
        print(i)