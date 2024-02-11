def solution(progresses, speeds):
    pro_days,answer = [],[]
    for i in range(len(progresses)):
        result=(100-progresses[i])/speeds[i]
        if result!=int(result):
            result=result+1
        pro_days.append(int(result))
        
    start,count=pro_days[0],0
    for i in range(len(pro_days)):
        if start>=pro_days[i]:
            count+=1
        else:
            answer.append(count)
            count,start=1,pro_days[i]
            
    answer.append(count)
    
    return answer
print(solution(list(map(int,input().split(','))),list(map(int,input().split(',')))))