#sorted한 결과를 프린트해야한다면 for문에 바로 sorted를 넣어보자!
#허용되는 크기보다 적게 신청할 수도 있다. 리스트는 용량보다 더 크게 끝 인덱스를 잡으면 알아서 모든 값을 반환하는걸 이용하자.

import sys
K,L=map(int,input().split())
s_list={}

for i in range(L):
    sincheong=sys.stdin.readline().strip()
    s_list[sincheong]=i

for final_list in sorted(s_list.items(),key=lambda x:x[1])[:K]:
    print(final_list[0])