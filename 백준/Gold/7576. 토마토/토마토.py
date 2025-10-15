import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int, input().split())))
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

visited = [[-1]*M for _ in range(N)]
def bfs():
    q = deque()
    for j in range(N):
        for i in range(M):
            if tomato[j][i] == 1:
                visited[j][i] = 0
                q.append((j, i))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0<=ny<N and 0<=nx<M):
                continue
            if visited[ny][nx] == -1 and tomato[ny][nx] != -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))

bfs()
ans = 0
for y in range(N):
    for x in range(M):
        if tomato[y][x] == -1:
            continue
        if visited[y][x] == -1:
            print(-1)
            sys.exit(0)
        ans = max(ans, visited[y][x])
        

print(ans)
