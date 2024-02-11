#문자열, 스택/큐?
N=int(input())

for k in range(N):
    string=list(input().split())
    rList=[]

    for word in string: #리스트에서 인덱스 헷갈림을 방지하기 위해 인덱스 변수이름 잘 짓기
        j=len(word)-1
        while j>=0:
            rList.append(word[j])
            j-=1
        rList.append(' ')

    print(''.join(rList))