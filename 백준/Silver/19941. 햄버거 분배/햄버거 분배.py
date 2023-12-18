import sys
N, K = map(int, sys.stdin.readline().split())
ham_people = list(sys.stdin.readline().strip())
answer=0

def is_Ham(idx):
    if idx>=0 and idx<len(ham_people) and ham_people[idx]=="H":
        ham_people[idx]="X"
        return True
    return False
    
for i,val in enumerate(ham_people):
    if val == "P":
        for j in range(i-K, i):
            if is_Ham(j): 
                answer+=1
                break
        else:
            for j in range(i+1, i+K+1):
                if is_Ham(j): 
                    answer+=1
                    break

print(answer)