def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0;
    
    queue = [begin];
    
    while queue:
        queue_size = len(queue)
        for _ in range(queue_size):
            current = queue.pop(0)
            if current == target:
                return answer
            for word in words:
                diff = 0
                for w,c in zip(word,current):
                    if w != c:
                        diff+=1
                if diff == 1:
                    queue.append(word)
        answer+=1
    
    return 0