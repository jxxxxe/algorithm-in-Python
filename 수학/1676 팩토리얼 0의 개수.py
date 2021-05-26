import sys

N=int(sys.stdin.readline().strip())

count=0
facto=1
for i in range(1,N+1):
    facto*=i

while facto%10==0:
    count+=1
    facto//=10

print(count)