import sys

input = sys.stdin.readline

N, M = map(int, input().split())
powers=[]

for _ in range(N):
    name, value = input().split()
    powers.append([name,int(value)])

for _ in range(M):
    power = int(input())
    left, right = 0, len(powers)-1
    while left<=right:
        mid = (left+right)//2
        if powers[mid][1]<power:
            left = mid+1
        else:
            right = mid-1
    print(powers[left][0])