import sys
def pado(n):
    soo=[1,1,1,2,2]
    for i in range(n-5):
        soo.append(soo[len(soo)-1]+soo[i])
    return soo

T,soo=int(input()),pado(100)
for _ in range(T):
    print(soo[int(sys.stdin.readline())-1])