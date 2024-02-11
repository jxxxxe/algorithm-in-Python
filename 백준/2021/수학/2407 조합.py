#https://www.acmicpc.net/problem/2407
#dp라 그래서 제외했더니만 아니었던 문제 ㅎ 우연히 발견하고 후다닥 데리고 옴
#조합0의 개수 문제 search하다가 조합관련해서 배웠다.
#일단, 팩토리얼 하고, 나누고 하는거다 보니 함수를 구현하는게 더 간편하고 깔끔
#nCm에서 n-m<m이면 m=n-m이라고 배워왔기 때문에 그렇게 썼는데 대부분 n//2<m을 쓰더라.
#결과값은 정수지만 나눗셈으로 인해 float형으로 나와서 형변환을 시켜줬었는데 애초에 나누기 할때 //를 쓰면 되는 것이었다;ㅎ
#m=0인 경우에 결과는 1이라고 따로 만들어줬었는데 생각해보니 어차피 result=1로 초기화를 무조건 해주기 때문에 필요 없는 부분이었다.

def factorial(a):
    result=1
    for i in range(a):
        result*=i+1
    return result

n,m=map(int,input().split())

if n//2<m:
    m=n-m

print(factorial(n)//(factorial(m)*factorial(n-m)))