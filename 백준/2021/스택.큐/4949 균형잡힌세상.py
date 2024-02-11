#여러테스트를 반복문으로 처리해야할 때 어떤 값/입력이 나올 때 종료된다는 조건을 할때 while 옆에 조건을 쓰면 해당 값이 들어와도 수행은 하고 종료됨
import sys

line=[]
stack=[]
error=0

while True:
    line=sys.stdin.readline().rstrip()
    if line=='.':
        break
    error=0
    stack=[]
    for l in line:
        if l=='(' or l=='[':
            stack.append(l)
        elif l==')' or l==']':
            if stack==[] or (l==')' and stack[-1]!='(') or (l==']' and stack[-1]!='['):
                error=1
                break
            stack.pop()
    if stack==[] and error==0:
        print("yes")
    else:
        print("no")