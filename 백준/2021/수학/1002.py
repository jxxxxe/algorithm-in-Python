#터렛

N=int(input())

for _ in range(N):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    d=((x1-x2)**2+(y1-y2)**2)**0.5
    radd=r1+r2
    rsub=abs(r1-r2)

    if x1==x2 and y1==y2 and r1==r2:
        print("-1")
    elif d>radd or d<rsub:
        print("0")
    elif d==rsub or d==radd:
        print("1")
    else:
        print("2")

#0: 두 중심점의 거리 > 반지름의 합 or 거리 < 차
#1: 거리=합 or 차
#2: 차<거리 or 거리<합(else)

