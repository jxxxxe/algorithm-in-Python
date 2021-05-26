#한수
def han(N):
    count=0
    
    for i in range(1,N+1):
        num=i
        list=[]
        while num!=0:
            list.append(num%10)
            num//=10
        
        if len(list)<=2:
            count+=1
            continue

        sub=list[1]-list[0]

        for j in range(2,len(list)):
         if sub!=list[j]-list[j-1]:
                count-=1
                break
        count+=1
    return count

N=int(input())
print(han(N))
    

