#https://www.acmicpc.net/problem/1515
import sys
N=input()

i=0
for j in range(1,sys.maxsize):
    for s in str(j):
        if N[i]==s:
            i+=1
        if i>=len(N):
            print(j)
            exit()