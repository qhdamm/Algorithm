import sys


input = sys.stdin.readline
n = int(input())
graph = [input().strip() for _ in range(n)]


dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

visited = [[False]*n for _ in range(n)]
def dfs(sy, sx):
    stack = [(sy, sx)]
    count = 0
    while stack:
        y, x = stack.pop()
        if visited[y][x]:
            continue
        visited[y][x] = True
        count += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<n:
                if graph[ny][nx] == "1" and not visited[ny][nx]:
                    stack.append((ny, nx))
    return count

house = []
for i in range(n):
    for j in range(n):
        if graph[j][i] == "1" and not visited[j][i]:
            house.append(dfs(j, i))

house.sort()
print(len(house))
for h in house:
    print(h)