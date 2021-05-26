#list.sort(), list.reverse() 자체는 리스트가 아님. 리스트의 상태를 바꾸는 일종의 명령문

list=list(map(int,input().split()))

otoe=[i for i in range(1,9)]

if list==otoe:
    print("ascending")
elif list==[9-i for i in otoe]:
    print("descending")
else:
    print("mixed")