import sys
from collections import Counter

trees=Counter(sys.stdin.read().split('\n')[:-1])

N=sum(list(trees.values()))

for key in sorted(trees.keys()):
    print(key,"%.4f"%(trees[key]/N*100))