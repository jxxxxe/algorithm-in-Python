import sys
N,assign=int(input()),[]
for _ in range(N):
    day,score=map(int,sys.stdin.readline().split())
    assign.append((day,score))

can={}
assign=sorted(assign,key=lambda x:(-x[1],x[0]))
for a in assign:
    index=a[0]-1
    if index not in can:
        can[index]=a[1]
    else:
        while index>=0 and index in can:
            index-=1
        if index>=0:
            can[index]=a[1]

print(sum(can.values()))