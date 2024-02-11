#yogurt.sort(reverse=True) => 리스트 역순으로 sort하기
#yogurt=[for]보다 yogurt=list(for)이 시간이 더 적게걸림.
#이상하게 여기는 N도 sys가 더 적게 걸리더라; 뭐 어쩌라는거임;;

import sys
N=int(sys.stdin.readline().strip())

yogurt=[int(sys.stdin.readline().strip()) for i in range(N)]

yogurt.sort(reverse=True)

sum=0
for i in range(N):
    if (i+1)%3==0:
        continue
    sum+=yogurt[i]

print(sum)