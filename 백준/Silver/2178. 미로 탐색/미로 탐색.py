import sys
from collections import deque


input = sys.stdin.readline
n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]

visited = [[0]*m for _ in range(n)]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)
ans = 0
def bfs(sx, sy):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] += 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if visited[ny][nx] == 0 and graph[ny][nx] == "1":
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))

bfs(0, 0)
print(visited[n-1][m-1])