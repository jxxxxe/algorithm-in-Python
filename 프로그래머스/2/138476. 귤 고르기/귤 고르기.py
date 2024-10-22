def solution(k, tangerine):
    total=0
    dic={}
    
    for tan in tangerine:
        if tan not in dic:
            dic[tan]=0
        dic[tan]+=1
        
    counts=sorted(dic.values(),reverse=True)

    for i,count in enumerate(counts):
        total+=count
        if total>=k:
            return i+1 
