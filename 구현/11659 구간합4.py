#구간들의 합을 구하는건 누적합을 이용한다! 미리 누적합을 리스트에 저장한 후 accums[j]-accums[i]로 한다!
#누적합을 편리하게 해주는 라이브러리~~~itertools.accumualte()!!
import sys
import itertools

N,M=map(int,sys.stdin.readline().split())
list_n=list(map(int,sys.stdin.readline().split()))

accums=list(itertools.accumulate(list_n))

for _ in range(M):
    i,j=map(int,sys.stdin.readline().split())
    print(accums[j-1]-accums[i-2]) if i>1 else print(accums[j-1])