#수찾기
#리스트는 순차적으로 값을 검색하기 때문에 시간복잡도O(n)
#집합(set)은 중복, 순서 없음. 값 검색 시 시간복잡도 O(1) => 한번에 찾음
#따라서 이 문제는 list를 쓰면 시간 초과, set을 써야함
N=int(input())
A=set(map(int,input().split()))

M=int(input())
list=list(map(int,input().split()))

for i in list:
    if i in A:
        print("1")
    else:
        print("0")