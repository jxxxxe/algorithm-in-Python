import sys

A,B=map(int,sys.stdin.readline().split())

sum=0
end=1
num=1
for i in range(1,B*B+1):
    if i==B+1:
        break
    if i>=A:
        sum+=num
        
    if i==end:
        num+=1
        end+=num

print(sum)