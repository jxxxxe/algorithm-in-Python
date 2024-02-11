#달팽이는 올라가고 싶다
A,B,V=map(int,input().split())

sub=A-B
day=(V-A)//sub+1
if (V-A)%sub>0:
    day+=1

print(day)
# while h<=V:
#     day+=1
#     h+=A
#     if h>=V:
#         break
#     h-=B      => 이 방법은 V의 값이 매우 커지면 오버타임됨;
