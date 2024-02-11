#이분탐색입니다만...이분탐색으로 안풀었습니다만...
import sys

N=int(input())
list_n=set(list(map(int,input().split())))
M=int(input())
list_m=list(map(int,input().split()))

for l in list_m:
    print("1",end=' ') if l in list_n else print("0",end=' ')