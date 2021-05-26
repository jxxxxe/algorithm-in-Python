#문자열 타입으로 된 숫자 i를 n의 자리수로 만들기(빈자리는 0을 채우기): i.zfill(n)
import sys

T=int(input())

for _ in range(T):
    sum=0
    h,w,n=map(int,sys.stdin.readline().split())
    for i in range(1,w+1):
        sum+=h
        if sum>=n:
            i=str(i).zfill(2)
            print("%s%s"%(h-(sum-n),i))
            break

       
       
        # 첨에 내가 했던 방법;; 현재 채워져있는 방과의 거리라고 착각함. 문제를 잘 읽어야 혀..
        # if sum>n:
        #     sum-=i
        #     print("%s0%s"%(n-sum+1,i))
        #     break
        # elif sum==n:
        #     print("10%s"%i)
        # sum+=i