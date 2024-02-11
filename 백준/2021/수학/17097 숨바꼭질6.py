#https://www.acmicpc.net/problem/17087
#a,b,c... 최대공약수 => gcd(a,b)와 c의 최대공약수...

def gcd(a,b):
    if b==0:
        return a
    if a<b:
        a,b=b,a
    return gcd(b,a%b)
    
N,S=map(int,input().split())
if N==1:
    print(abs(S-int(input())))
    exit()

diff=list(map(int,input().split()))
diff=list(abs(d-S) for d in diff)

GCD=gcd(diff[0],diff[1])
for i in range(2,N):
    GCD=gcd(GCD,diff[i])

print(GCD)