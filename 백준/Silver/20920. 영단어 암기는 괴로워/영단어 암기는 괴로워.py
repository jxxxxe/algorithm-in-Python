import sys
from collections import defaultdict

N, leng = map(int, input().split())
word_counter = defaultdict(int)
for _ in range(N):
    word = sys.stdin.readline().strip()
    if len(word) >= leng:
        word_counter[word]+=1

word_counter = sorted(word_counter.items(), key=lambda word: (-word[1], -len(word[0]), word[0]))

for word, i in word_counter:
    print(word)