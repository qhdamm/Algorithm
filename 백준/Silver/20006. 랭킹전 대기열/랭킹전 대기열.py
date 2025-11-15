import sys

input = sys.stdin.readline
p, m = map(int, input().split())

rooms = []
for _ in range(p):
    level, name = input().split()
    level = int(level)
    flag = False
    for room in rooms:
        room_level = room[0][0]
        if len(room) < m and abs(level - room_level) <= 10:
            room.append((level, name))
            flag = True
            break
    
    if not flag:
        rooms.append([(level, name)])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    room.sort(key=lambda x: x[1])
    for level, name in room:
        print(level, name)