while True:
    money=int(input("투입 금액 입력: "))
    if money<0:
        break
    N=int(input("음료수의 갯수 입력: "))
    if money<N*1000:
        add=input("금액 부족. 추가 입금 하시겠습니까?(Y/N): ")
        if add=='Y':
            money+=int(input("추가 금액 입력: "))
        if money<N*1000:
            print("@금액이 부족합니다.")
            continue
    print("@입력한 총 금액:%d"%money)
    print("@구매한 총 금액:%d"%(N*1000))
    print("@거스름돈:%d"%(money-N*1000))
    print("@구매한 음료수 개수:%d"%N)