from collections import Counter

N=int(input())
target = Counter(input().strip())
answer = 0

for _ in range(N-1):
    word=Counter(input().strip())
    if len(list((word-target).elements()))<=1 and len(list((target-word).elements()))<=1:
        answer+=1

print(answer)