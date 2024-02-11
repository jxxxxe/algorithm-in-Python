import sys

T=int(input())

for _ in range(T):
    command,current=sys.stdin.readline().strip(),[0,0]
    dir,max_xy,min_xy=0,[0,0],[0,0]
    for c in command:
        if (c=='F' and dir%4<2) or (c=='B' and dir%4>=2):
            current[dir%2]+=1
            max_xy[dir%2]=max(current[dir%2],max_xy[dir%2])
        elif (c=='B' and dir%4<2) or (c=='F' and dir%4>=2):
            current[dir%2]-=1
            min_xy[dir%2]=min(current[dir%2],min_xy[dir%2])
        elif c=='L':
            dir+=3
        elif c=='R':
            dir+=1
    print((max_xy[0]-min_xy[0])*(max_xy[1]-min_xy[1]))