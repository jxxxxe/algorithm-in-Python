N=input()

n=1
total=0

while n<len(N):
    total+=n*9*10**(n-1)
    n+=1

total+=len(N)*(int(N)-10**(len(N)-1)+1)  

print(total)