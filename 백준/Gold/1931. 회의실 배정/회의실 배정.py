# 지금 시점에서 가장 빨리 끝나는 회의 선택
import sys

input = sys.stdin.readline
N = int(input())
room_list = []
for _ in range(N):
    room_list.append(list(map(int, input().split())))

# list의 각 원소 x에서 두번째, 첫번째 값을 뽑아서 정렬
room_list.sort(key=lambda x: [x[1], x[0]])
current_time = 0
ans = 0
for room in room_list:
    if current_time <= room[0]:
        ans += 1
        current_time = room[1]
print(ans)