from collections import Counter
N,A=int(input()),list(map(int,input().split()))

counter,increase,sort=Counter(A),[],sorted(A)

for a in A:    
    counter[a]-=1
    sort.remove(a)
    if a in increase:
        continue
    while increase and increase[-1]>a and counter[increase[-1]]>0:
        increase.pop()
    if not increase or increase[-1]<a:
        increase.append(a)

print(len(increase))
for i in increase:
    print(i,end=' ')