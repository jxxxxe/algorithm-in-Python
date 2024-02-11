#직각삼각형
while True:
    line=list(map(int,input().split()))     #반복문으로 계속 리스트를 받을 때 리스트 이름을 list로 하면 안되더라ㅇㅅㅇ
    if line[0]==0 and line[1]==0 and line[2]==0:
        break
    line.sort()
    if line[0]**2+line[1]**2==line[2]**2:
        print("right")
    else:
        print("wrong")