#소인수분해

N=int(input())

while N%2==0 and N>1:
    print("2")
    N//=2

k=N
i=1
while i <N:
    if k<=1:
        break
    if k%(2*i+1)==0:
        print(2*i+1)
        k//=(2*i+1)
        i-=1
    i+=1
# for i in range(1,N): i-=1한다고 해서 i가 증가하지 않는 것이 아니더라? while문을 써야햇음;