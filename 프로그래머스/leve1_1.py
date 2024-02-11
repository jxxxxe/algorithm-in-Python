n=int(input())
lost=list(map(int,input().split()))
reserve=list(map(int,input().split()))

answer = n-len(lost)
mine=set(lost)&set(reserve)
for m in mine:
    lost.remove(m)
    reserve.remove(m)
    answer+=1
for l in lost:
    for r in reserve:
        if abs(r-l)<=1:
            answer+=1
            reserve.remove(r)
            break
print(answer)