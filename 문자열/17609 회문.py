#앞과 끝을 같은 변위 만큼 뗄 때 str[i:-i] <<이런 방식을 쓰려고 할 수 있는데 i=0일 땐 문자열이 탄생하지 못하므로 이 방식은 쓰지 말아야 함
#인덱스 i번째 부터/까지 회문인지 검사할땐 str[i:]==str[i:][::-1] / str[:-i]==str[:-i][::-1]를 쓰면 된다. 
import sys
N=int(input())

for _ in range(N):
    str=sys.stdin.readline().strip()
    if str==str[::-1]:
        print(0)
        continue

    code1=0
    for i in range(len(str)//2):
        if str[i]!=str[-(i+1)]:
            check=str[i:len(str)-i]
            if check[1:]==check[1:][::-1] or check[:-1]==check[:-1][::-1]:
                code1=1
            break
    print(1) if code1==1 else print(2)