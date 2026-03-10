import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
tomato = []
for _ in range(h):
    layer = []
    for _ in range(n):
        layer.append(list(map(int, input().split())))
    tomato.append(layer)

dy = (0, 0, 1, -1, 0, 0)
dx = (1, -1, 0, 0, 0, 0)
dh = (0, 0, 0, 0, 1, -1)
visited = [[[-1]*m for _ in range(n)] for _ in range(h)]
q = deque()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomato[z][y][x] == 1:
                q.append((z, y, x))
                visited[z][y][x] = 0


def bfs():
    while q:
        ch, cy, cx = q.popleft()
        for i in range(6):
            nh = ch + dh[i]
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=nx<m and 0<=ny<n and 0<=nh<h:
                if tomato[nh][ny][nx] == 0 and visited[nh][ny][nx] == -1:
                    q.append((nh, ny, nx))
                    visited[nh][ny][nx] = visited[ch][cy][cx] + 1

bfs() 
ans = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0 and visited[i][j][k] == -1:
                print(-1)
                exit()
            ans = max(ans, visited[i][j][k])
print(ans)