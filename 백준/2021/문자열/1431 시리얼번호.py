#re라이브러리를 사용해서 숫자를 추출하는 것보다 문자 하나하나 체크하는 것이 더 적게 걸림.
import sys

N=int(input())

guitar=[]
for _ in range(N):
    string=sys.stdin.readline().strip()
    sum=0
    for n in string:
        if n.isdigit():
            sum+=int(n)
    guitar.append((string,sum))

for g in sorted(guitar,key=lambda x:(len(x[0]),x[1],x[0])): 
    print(g[0])