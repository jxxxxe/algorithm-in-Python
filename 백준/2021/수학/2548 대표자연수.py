#https://www.acmicpc.net/problem/2548
#-_-..
#차이가 가장 적은.. => 중앙값
#중앙값인건 ㅇㅇ 진즉 알았다고. 근데 보통 중앙값은 개수가 짝수일땐 중간 두개 값의 평균인데
#여기는 리슽트 안에서 대표를 뽑는거니 걍 중간 두개값 중 먼저 나오는 값이 중앙값 ㅇㅅㅇ
#저 사실 땜에 몇번을 틀렸는지 원.. 구글링으로 결국 도움을 받았다고 한다(분하다)
import sys

N=int(input())

nums=list(map(int,sys.stdin.readline().split()))
nums.sort()

print(nums[N//2-1]) if N%2==0 else print(nums[N//2])