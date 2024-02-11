import sys

list=[int(sys.stdin.readline().strip()) for _ in range(8)]

orig=list[::]
list.sort()

print(sum(list[3:]))
for i in range(8):
    if not orig[i] in list[:3]:
        print(i+1,end=' ')