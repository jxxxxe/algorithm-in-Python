def solution(answers):
    result = [0,0,0]
    supo_answers = [[1,2,3,4,5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    for idx, answer in enumerate(answers):
        for supo_idx, supo_arr in enumerate(supo_answers):
            result[supo_idx] += (answer == supo_arr[idx%len(supo_arr)])
    
    best = []
    max_result = max(result)
    
    for i in range(len(result)):
        if max_result == result[i]:
            best.append(i+1)
    
    return best