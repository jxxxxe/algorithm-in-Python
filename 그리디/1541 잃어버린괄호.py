e,result,tmp,j=input(),0,0,0
for i in range(len(e)-1,-1,-1):
    if e[i].isdigit():
        tmp+=int(e[i])*10**j
        j+=1
        continue
    if e[i]=='-':
        result-=tmp
        tmp=0
    j=0

print(result+tmp)