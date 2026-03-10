import sys

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_h = max(map(max, graph))

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

def dfs(y, x, h, visited):
    stack = [(y, x)]
    visited[y][x] = True
    while stack:
        cy, cx = stack.pop()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=nx<n and 0<=ny<n and graph[ny][nx]> h and not visited[ny][nx]:
                visited[ny][nx] = True
                stack.append((ny, nx))

answer = 0

for h in range(max_h+1):
    visited = [[False]*n for _ in range(n)]
    cnt = 0

    for y in range(n):
        for x in range(n):
            if not visited[y][x] and graph[y][x] > h:
                dfs(y, x, h, visited)
                cnt += 1
    
    answer = max(answer, cnt)
print(answer)