N=int(input("N입력: "))

for i in range(1,101):
    print(str(i)+" : ",end='')
    if i%10==N and (i//10)%10==N:
        print("짜짝")
    elif i%10==N or (i//10)%10==N or i%N==0:
        print("짝")
    else:
        print()