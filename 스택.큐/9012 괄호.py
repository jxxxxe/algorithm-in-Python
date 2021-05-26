#공백없이 입력되는 문자열은 리스트에 분리되어 저장되지 x
#두개의 리스트를 같이 쓸 땐 서로 혼동하지 않게 주의
#한번 실행에서 여러개의 테스트케이스가 입력되는 경우에는 쓰이는 리스트/변수를 적절히 초기화
import sys

N=int(input())
list=[]

for _ in range(N):
    stack=[]
    list=sys.stdin.readline().strip()
    for p in list:
        if p=='(':
            stack.append(p)
        elif p==')':
            if stack==[]:
                stack.append(-1)
                break
            else:
                stack.pop()
    if stack==[]:
        print("YES")
    else:
        print("NO")