#셀프넘버
#d(n)은 각자리수에 n도 더해줘야함을 잊지말자

list=[]
for i in range(1,10001):
    n=i
    sum=n
    while n!=0:
        sum+=n%10
        n//=10
    list.append(sum)

for i in range(1,10001):
    if not i in list:
        print(i)