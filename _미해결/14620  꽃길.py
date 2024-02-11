def overlap(x,y,band):
    if (x,y) in band or (x-1,y) in band or (x+1,y) in band or (x,y-1) in band or (x,y+1) in band:
        return True
    return False

def make_band(x,y):
    band=set()
    band.add((x-1,y))
    band.add((x+1,y))
    band.add((x,y-1))
    band.add((x,y+1))
    return band

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
        prices.append((f_price[i][j]+f_price[i-1][j]+f_price[i][j-1]+f_price[i+1][j]+f_price[i][j+1],i+1,j+1))

prices.sort()
value=sum(prices[-3:][0])
for i in range(len(prices)-2):
    if i>=len(prices)-2:
        break
    no_set=make_band(prices[i][1],prices[i][2])
    for j in range(i+1,len(prices)-1):
        if j>=len(prices)-1:
            break
        if overlap(prices[j][1],prices[j][2],no_set):
            continue
        no_set2=make_band(prices[j][1],prices[j][2])
        for k in range(j+1,len(prices)):
            if not overlap(prices[k][1],prices[k][2],no_set) and not overlap(prices[k][1],prices[k][2],no_set2):
                value=min(value,prices[i][0]+prices[j][0]+prices[k][0])
                prices=prices[:k+1]
                break

print(value)