#문자열 reverse, reversed안됨
#대신 슬라이싱이 있다!!!!!!!!!!!!
#N,M을 int로 map안하고 받는것보다 하는게 더 빨랐다; 쩝
def Rev(a):
    return int(str(a)[::-1])
N,M=map(int,input().split())
print(Rev(Rev(N)+Rev(M)))