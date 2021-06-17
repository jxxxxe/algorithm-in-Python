import sys
N=int(input())
timetable=[]
for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    timetable.append((a,b))

timetable.sort()

print(timetable)