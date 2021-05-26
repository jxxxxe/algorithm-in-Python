import sys

N=int(sys.stdin.readline().strip())
num=int(sys.stdin.readline().strip())
for i in range()
jarisu=
if num==0:
    print(min(len(N),abs(N-100)))
    exit()
error=set(map(int,input().split()))
if num==10:
    print(abs(N-100))
    exit()
button=list(set(i for i in range(10))-error)

count=0
channel=-1

jari=[N%(10*i) for i in range(len(N))]
jari.reverse()

i=0
while channel<N:
    copy=[abs(jari[i]-b) for b in button]
    m=min(copy)

    if i>0 and copy.count(m)>1:
        x=copy.index(m,x)
    else:
        x=copy.index(m)
    channel*=10**i
    channel+=button[x]
    i+=1

channel//=10
count=len(n)+abs(N-channel)

print(min(count,abs(N-100)))