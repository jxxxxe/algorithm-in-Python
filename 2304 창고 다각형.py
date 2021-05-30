#값 두개 이상이나 map은 한번에 리스트에 넣을 수 x
import sys

N=int(input())

column=[]

for i in range(N):
    L,H=map(int,sys.stdin.readline().split())
    column.append((L,H))

if N==1:
    print(column[0][1])
    exit()

column.sort()
pre_L,max_h=column[0][0],column[0][1]
total=0

for i in range(1,N):
    if i==N-1:
        if max_h>column[i][1]:  #마지막 기둥의 높이가 최고가 아니라면
            total+=(column[i][0]-pre_L+1)*column[i][1]
            total+=max_h-column[i][1]
            break
        else: #마지막 기둥의 높이가 최고라면
            pre_L-=1
            total+=column[i][1]-max_h
        
    if max_h<=column[i][1]:
        total+=(column[i][0]-pre_L)*max_h
        pre_L,max_h=column[i][0],column[i][1]
    
print(total)