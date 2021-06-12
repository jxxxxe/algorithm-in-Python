#첨엔 자리수 따로따로 매칭 했는데 브루트포스 rgrg?..
#고장난 버튼이 없을 수도 있다 >> 고장버튼의 입력이 안올수도 있음을 따로 구현해줌
#set a는 set b의 부분집합인가 ? => if set(a) == b.intersection(a)
#N보다 작은 수의 버튼과 높은 수의 버튼의 반복문을 따로 구현..why? 끝나는 지점이 다르기 때문!
#N보다 작은 수의 버튼과 높은 수의 버튼의 초기화 => 반복문을 거칠 수도 아닐수도 있어서 초기화를 해줘야 하는데
                                                #마지막에 비교를 해야하니 고것으로 초기화하면 되지롱
N,num=int(input()),int(input())
btns=set(list(range(10)))
if num!=0:
    btns-=set(map(int,input().split()))
btns=set(map(str,btns))
btn_min,btn_max=abs(100-N),abs(100-N)

for i in range(N+1):
    if set(str(N-i)) == btns.intersection(set(str(N-i))):
        btn_min=i+len(str(N-i))
        break

i=0
while i+len(str(N+i))<abs(100-N):
    if set(str(N+i)) == btns.intersection(set(str(N+i))):
        btn_max=i+len(str(N+i))
        break
    i+=1

print(min(btn_min,btn_max,abs(100-N)))