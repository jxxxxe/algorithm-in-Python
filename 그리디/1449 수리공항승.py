#12 line) 원랜 l+0.5가 커버안에 들어오는지 확인하는게 정확한거지만 테이프 길이는 자연수이므로 l을 막으면=l+0.5도 막는것
#고작 +0.5 더 붙였다고 속도 45 더 나가는거 실화?
import sys

N,L=map(int,input().split())
leak=list(map(int,sys.stdin.readline().split()))
leak.sort()

cover=leak[0]+L-0.5
count=1
for l in leak:
    if l+0.5<=cover:    
        continue
    else:
        cover=l+L-0.5
        count+=1

print(count)