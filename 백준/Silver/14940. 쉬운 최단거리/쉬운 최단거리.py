import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lands = []
for _ in range(n):
    lands.append(list(map(int, input().split())))

visited = [[-1]*m for _ in range(n)]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if lands[ny][nx] == 0:
                    continue
                elif visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
            
y = x = -1
for i in range(n):
    for j in range(m):
        if lands[i][j] == 2:
            y, x = i, j

bfs(y, x)

for i in range(n):
    row = []
    for j in range(m):
        if lands[i][j] == 0:
            row.append(0)
        else:
            row.append(visited[i][j])
    print(*row)