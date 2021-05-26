N,M=map(int,input().split())

def revadd(N):
    Rn=0
    while N>0:
        Rn=Rn*10+N%10
        N//=10
    return Rn

print(revadd(revadd(N)+revadd(M)))