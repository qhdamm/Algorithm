import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(input().strip())

visited = [[0]*M for _ in range(N)]
def bfs():
    queue = deque()
    queue.append((0,0))
    visited[0][0] += 1

    dy = (0, 0, 1, -1)
    dx = (1, -1, 0, 0)
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M:
                if visited[ny][nx] == 0 and arr[ny][nx] == "1":
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))

bfs()
print(visited[N-1][M-1])

