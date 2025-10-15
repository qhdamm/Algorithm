import sys
from collections import deque
input = sys.stdin.readline


t = int(input())
dy = (1, 2, 2, 1, -1, -2, -2, -1)
dx = (-2, -1, 1, 2, 2, 1, -1, -2)


def bfs(sx, sy, ex, ey):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = 0
    
    while q:
        y, x = q.popleft()
        if y == ey and x == ex:
            return visited[y][x]
        
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0<=ny<n and 0<=nx<n):
                continue

            if visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))

for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    visited = [[-1]*n for _ in range(n)]
    
    ans = bfs(sx, sy, ex, ey)
    print(ans)
