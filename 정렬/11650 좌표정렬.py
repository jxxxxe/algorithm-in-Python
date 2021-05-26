spot={}

N=int(input())

for i in range(N):
    x,y=input().split()
    if x in spot:
        spot[x]=[spot[x],y]
    else:
        spot={x:y}
    print(spot.keys," : ",spot.values)