N,M=map(int,input().split())

line=[]

for _ in range(N):
    line.append(input())

list=["BWBWBWBW","WBWBWBWB"]

min=64
for col in range(N-7):
    for row in range(M-7):
        for h in range(2):
            count=0
            k=h
            for i in range(8):
                for j in range(8):
                    count+=(line[col+i][row+j]!=list[k%2][j])
                k+=1
            if min>count:
                min=count
            
print(min)

'''
import sys
from itertools import accumulate as acc
input = sys.stdin.readline
N, M=map(int,input().split())
dat = [[0]*(M+1)]
for i in range(N):
  a=[0]
  a.extend(acc([((dat=='B')+i+j)%2 for j,dat in enumerate(input())]))
  dat.append([j+k for j,k in zip(dat[-1],a)])
temp=64
for i in range(N-7):
  for o in range(M-7):
    ans=dat[i+8][o+8]+dat[i][o]-dat[i][o+8]-dat[i+8][o]
    temp=min(ans,64-ans,temp)
print(temp)3e
'''