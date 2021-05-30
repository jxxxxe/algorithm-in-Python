#https://www.acmicpc.net/problem/1713
#dict,set의 삭제는 O(1)
#min(사전) 하면 사전 value의 최소값을 반환
#defaultdict 라이브러리 편하긴 하지만 속도면에선 그냥 직접 초기화 코드 짜는게 훨씬 더 좋았다.
#사전 초기화에서 stud_reco[s]=0를 최소값 찾기 전에 했더니 당연히 최소값은 새로 들어온 애가 됐고 set엔 없으니 오류가 났다. 이런 실수는 하지 말자
#다른 사람들은 stud_reco, final 다 리스트로 구현해서 index를 맞췄다. 이렇게 해도 속도는 같았다.
import sys

N=int(input())
reco=int(input())
stud=list(map(int,sys.stdin.readline().split()))

stud_reco={}
final=set()

for s in stud:
    if not s in final:
        if len(final)==N:
            min=reco+1
            for key,value in stud_reco.items():
                if value<min:
                    min=value
                    min_stu=key
            final.remove(min_stu)
            del stud_reco[min_stu]
        stud_reco[s]=0

    final.add(s)
    stud_reco[s]+=1

for f in sorted(final):
    print(f,end=' ') 