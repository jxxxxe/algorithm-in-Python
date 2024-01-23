import sys

N = int(input())
sticks = {}

for _ in range(N):
    x,y= map(int,sys.stdin.readline().split())
    sticks[x]=y

lx, rx = min(sticks), max(sticks)
ly_max, ry_max = sticks[lx], sticks[rx]

result=0

while lx <= rx:
    if lx in sticks:
        ly_max = max(ly_max, sticks[lx])
    if rx in sticks:
        ry_max = max(ry_max, sticks[rx])

    if ly_max<=ry_max:
        result+=ly_max
        lx+=1
    else:
        result+=ry_max
        rx-=1

print(result)