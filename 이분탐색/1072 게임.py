#https://www.acmicpc.net/problem/1072
#나눗셈 결과를 int형으로 형변환 하는건 위험하다. //를 이용하자
#(100+y)/x => O      y/x*100 => X
#이진탐색 => left, mid, right //left>=right이면 종료
#(중요!) 승률이 바뀌는게 꼭 +1이 최소는 아니다!!!!!!!
X,Y=map(int,input().split())
max=1000000000

if X==Y or 100*(Y+max)//(X+max)==100*Y//X:
    print(-1)
    exit()

Z=100*Y//X
left,right=0,max

while True:
    mid=(left+right)//2
    winper=100*(Y+mid)//(X+mid)
    if winper<=Z:
        left=mid+1
    else:
        right=mid
    if left>=right:
        break

print(right)