import sys

input = sys.stdin.readline

n=int(input())
heights=list(map(int,input().split()))

answer=[0]*n
for i in range(n):
    for j in range(i+1,n):
        for k in range(i+1,j):
            if (heights[i]-heights[j])/(i-j)*(k-i)+heights[i] <= heights[k]:
                break
        else:
            answer[i]+=1
            answer[j]+=1

print(max(answer) if n>1 else 0)