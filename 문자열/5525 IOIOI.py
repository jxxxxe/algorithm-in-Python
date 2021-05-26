import sys

N=int(sys.stdin.readline().strip())
M=int(sys.stdin.readline().strip())
list=sys.stdin.readline().strip()

i=0
char="IO"*N+"I"
while True:
    index=list.find(char)
    if index==-1:
        print(i)
        break
    list=list[index+:]
    i+=1