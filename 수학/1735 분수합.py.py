#역시 .. 반복문 없이 정해진 개수의 숫자들은 sys보다 input이 더 적게 걸림
import sys

a1,b1=map(int,input().split())
a2,b2=map(int,input().split())

ha,hb=(a1*b2+a2*b1),b1*b2
a,b=ha,hb
while b>0:
    if a<b:
        a,b=b,a
    a,b=b,a%b

print("%s %s"%(ha//a,hb//a))