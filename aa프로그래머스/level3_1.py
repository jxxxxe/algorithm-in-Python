def solution(A, B):
    i,j,answer=0,0,0
    A.sort()
    B.sort()
    while i<len(A) and j<len(B):
        if A[i]>=B[j]:
            j+=1
            continue
        answer+=1
        i+=1
        j+=1
    return answer