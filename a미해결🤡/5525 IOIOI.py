#for문 안에서 어떤 짓을 해도 for문의 i는 자기 갈길을 간다.(한번 돌 때마다 +1 된다는 말)
import sys

N=int(input().strip())
M=int(input().strip())
S=sys.stdin.readline().strip()

count_O=0
count=0
i=1
while i<M:
    if S[i-1]=='I':
        while i<M and S[i-1]!=S[i]:
            if S[i]=='O':
                count_O+=1
            i+=1
        if count_O>2 and S[i-1]=='O' and S[i]=='O':
            count_O-=2
        count+=count_O-N+1
        count_O=0
    i+=1

print(count)