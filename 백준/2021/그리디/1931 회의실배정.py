import sys
N=int(input())
timetable=[]
for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    timetable.append((a,b))

timetable.sort()
end,count=timetable[0][1],1
for i in range(1,len(timetable)):
    if timetable[i][0]<end and timetable[i][1]>end:
        continue
    if timetable[i][0]>=end:
        count+=1
    end=timetable[i][1]
    
print(count)