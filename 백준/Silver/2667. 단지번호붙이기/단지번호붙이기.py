import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n):
    graph.append(input().strip())

visited = [[False]*n for _ in range(n)]
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
home = []
def dfs(y, x):
    global num
    visited[y][x] = True
    num += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and graph[ny][nx] == "1":
            dfs(ny, nx)
    return num


for y in range(n):
    for x in range(n):
        if not visited[y][x] and graph[y][x] == "1":
            num = 0
            dfs(y, x)
            home.append(num)

print(len(home))
home.sort()
for h in home:
    print(h)