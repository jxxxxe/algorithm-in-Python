#유클리드호제법
#최대공약수: a=b, b=a%b 해서 b가 0이 될 때까지(중간에 a<b이면 a,b자리 바꿈)
#최소공배수: 두수의 곱/최대공약수
#<파이썬> a,b=b,a+1 일때 b를 연산할 때는 원래 a 값을 기준으로 연산이 된다.(ssaengU~)
N,M=map(int,input().split())

a=N
b=M
while b>0:
    if a<b:
        a,b=b,a
    a,b=b,a%b

gcd=a
lcm=(N*M)//gcd

print(gcd)
print(lcm)