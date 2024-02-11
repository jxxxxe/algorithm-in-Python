def facto(a):
    result=1
    for i in range(a):
        result*=i+1

    return result

N=int(input())

line=list(map(int,input().split()))
case=line[0]

remain=list(range(1,N+1))
if case==1:
    zari,result,k,=len(remain),[],line[1]-1
    for z in range(zari,0,-1):
        num=k//facto(z-1)
        result.append(remain[num])
        k%=facto(z-1)
        del remain[num]
    print(' '.join(map(str,result)))
    
elif case==2:
    soon=line[1:]
    count=0
    for s in soon:
        remain.remove(s)
        for r in remain:
            if r>s:
                break
            count+=facto(len(remain))
    print(count+1)