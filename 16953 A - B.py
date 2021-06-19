#왜때문 그래프임.. 그래둥절
def a_to_b(a,b):
    i=1
    while a!=b:
        i+=1
        if b%2==0:
            b//=2
        else:
            if b%10!=1:
                return -1
            b//=10
        if a==b:
            return i
        elif a>b:
            return -1

a,b=map(int,input().split())
print(a_to_b(a,b))