N=int(input())

if N%4==0 or N%4==2:
    print("SK") if (N//4)%2==1 else print("CY")
elif N%4==1 or N%4==3:
    print("SK") if (N//4)%2==0 else print("CY") 