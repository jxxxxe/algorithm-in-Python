import sys

p, avail  = map(int,input().split())

rooms = []
for _ in range(p):
    level, nickname = sys.stdin.readline().split()
    level = int(level)

    idx = len(rooms)

    #해당하는 방 찾기
    for index,room in enumerate(rooms):
        if room[0][0] - 10 <= level <= room[0][0]+10 and len(room)<avail:
            idx = index
            break  
    else:
        rooms.append([])
        index = len(rooms)-1
    
    #결과에 플레이어 이름 등록
    rooms[index].append([level,nickname])

# 플레이어 정렬 및 출력
for room in rooms:
    room.sort(key=lambda x: x[1])

    if len(room) == avail:
        print("Started!")
    else:
        print("Waiting!")
    
    for player in room:
        print(player[0],player[1])