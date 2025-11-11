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

q = deque()
visited = [[[-1]*m for _ in range(n)] for _ in range(h)]
for k in range(h):
    for j in range(n):
        for i in range(m):
            if tomato[k][j][i] == 1:
                q.append((k, j, i))
                visited[k][j][i] = 0

while q:
    hi, yi, xi = q.popleft()
    for d in range(6):
        nh = hi + dh[d]
        ny = yi + dy[d]
        nx = xi + dx[d]
        if 0<=nh<h and 0<=ny<n and 0<=nx<m:
            if tomato[nh][ny][nx] == 0 and visited[nh][ny][nx] == -1:
                visited[nh][ny][nx] = visited[hi][yi][xi] + 1
                tomato[nh][ny][nx] = 1
                q.append((nh, ny, nx))

ans = 0
for k in range(h):
    for j in range(n):
        for i in range(m):
            if tomato[k][j][i] == 0:
                print(-1)
                sys.exit(0)
            ans = max(ans, visited[k][j][i])
print(ans)