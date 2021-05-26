X,Y=map(int,input().split())

Z=int(Y/X*100)
n=0
while True:
    winper=int((Y+n)/(X+n)*100)
    if Z+1<=winper or winper>=100:
        break
    n+=10
print(n if n else -1)