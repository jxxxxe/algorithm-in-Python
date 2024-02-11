#올림 필요 없이 a-=a//2; b-=b//2 로 하믄 됨.. 신기..방기..동방신기..
def up(n):
    if n/2!=n//2:
        return (n//2)+1
    return n//2

N,a,b=map(int,input().split())
i=0
while a!=b:
    a,b=up(a),up(b)
    i+=1

print(i)