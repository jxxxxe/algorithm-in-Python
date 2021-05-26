#시간초과
T=int(input())

for _ in range(T):
    key=input()
    password=[]
    index=0
    for k in key:
        if k=='<':
            if index==0:
                continue
            index-=1
        elif k=='>':
            if index==len(password):
                continue
            index+=1
        elif k=='-' and len(password)>=1:
            password=password[:len(password)-1]
        else:
            password.insert(index,k)
            index+=1
    for p in password: print(p,end='')
    print("")