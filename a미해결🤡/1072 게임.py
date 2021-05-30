X,Y=map(int,input().split())

Z=int(Y/X*100)
min,max=0,1000000000

while True:
    n=(min+max)//2
    winper=int((Y+n)/(X+n)*100)
    if winper>Z+1:
        max//=2
        continue
    elif winper<Z+1:
        min+=max-min
        max+=max-min
    if Z+1==winper or winper>=100:
        break
print(min)
# for n in range(min,n+1):
#     winper=int((Y+n)/(X+n)*100)
#     if winper==Z+1:
#         break

print(n if n else -1)