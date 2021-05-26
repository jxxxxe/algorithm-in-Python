#사전 두개 말고 한개는 리스트로 해서 찾으려는게 정수면 인덱스를 불러 하는게 살짝 더 빨랐음
#두개의 정수를 연달아 입력받을 땐 input보다 readline이 더 빨랐음
#입력받을 때 map,split,strip 혼동하지 말 것

import sys
N,M=map(int,input().split())

keynum={}
keyeng={}
for i in range(N):
    monster=sys.stdin.readline().strip()
    keynum[str(i+1)]=monster
    keyeng[monster]=i+1

for _ in range(M):
    find=sys.stdin.readline().strip()
    if find in keynum:
        print(keynum[find])
    else:
        print(keyeng[find])