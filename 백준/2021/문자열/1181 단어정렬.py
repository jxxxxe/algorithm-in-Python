#사전을 값으로 정렬: sorted(word.items(),key=lambda x : x[1])
#다중조건으로 한번에 정렬하기!: sorted(e, key = lambda x : (len(x[0]),x[0], -x[1])) :key길이오름차순->key오름차순->value내림차순 으로 정렬
#사전을 sorted하면 튜플(키,값)의 리스트 형태가 됨

#다중조건보단 리스트에 담고 정렬하고 len조건으로 정렬하는게 조금 더 빨랐음
#첨에 정수하나 입력 받을 때는 sys보다 input()이 더 빠르고, 반복문으로 여러개 문자 입력받을 땐 sys가 월등히 빠르다.

import sys

N=int(input())

word=set([sys.stdin.readline().strip() for _ in range(N)])

word=sorted(word, key=lambda x : (len(x),x))

for k in word:
    print(k)


#첨에 내가 했던 방법(set로 중복제거"->리스트->리스트로 알파벳정렬->사전에 글자수랑 담기"->value로 정렬)
'''
import sys

N=int(sys.stdin.readline().strip())

set=set([input() for _ in range(N)])

list=list(set)
list.sort()

word={}
for i in list:
    word[i]=len(i)

sword=sorted(word.items(),key=lambda x : x[1])

for k in sword:
    print(k[0])
'''