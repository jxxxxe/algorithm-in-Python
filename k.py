import sys
N=int(input())

f_price=[[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    line=list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        f_price[i][j]=line[j]

prices=[]
for i in range(1,N-1):
    for j in range(1,N-1):
        prices.append((f_price[i][j]+f_price[i-1][j]+f_price[i][j-1]+f_price[i+1][j]+f_price[i][j+1],i,j))

prices.sort()

min=prices[-1][0]
for i in range(N):
    if prices[i][0]>min:
        break

    final=[]
    f1_x,f1_y=prices[i][1],prices[i][2]
    final.append(prices[i])
    for j in range(i+1,len(prices)):
        if (f1_x==prices[j][1] and abs(f1_y-prices[j][2])<3) or (f1_y==prices[j][2] and abs(f1_x-prices[j][1])<3):
            continue
        if abs(f1_x-prices[j][1])==1 and abs(f1_y-prices[j][2])==1:
            continue

        if len(final)==2:
            f2_x,f2_y=final[1][1],final[1][2]
            if (f2_x==prices[j][1] and abs(f2_y-prices[j][2])<3) or (f2_y==prices[j][2] and abs(f2_x-prices[j][1])<3):
                continue
            if abs(f2_x-prices[j][1])==1 and abs(f2_y-prices[j][2])==1:
                continue

        final.append(prices[j])
        if len(final)==3:
            break
    
    if min>final[0][0]+final[1][0]+final[2][0]:
        min=final[0][0]+final[1][0]+final[2][0]
    
print(min)