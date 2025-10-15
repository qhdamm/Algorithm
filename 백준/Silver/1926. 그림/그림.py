import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = []
cnt = 0
visit_num = 0
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False]*m for _ in range(n)]
def dfs(y, x):
    visit_num = 1
    visited[y][x] = True
    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not (0<=nx<m and 0<=ny<n):
            continue
        if visited[ny][nx] == False and arr[ny][nx] == 1:
            visit_num += dfs(ny, nx)
    return visit_num
        


max_visit = 0
for j in range(n):
    for i in range(m):
        if arr[j][i] == 1 and visited[j][i] == False:
            visit_num = dfs(j, i)
            max_visit = max(max_visit, visit_num)
            cnt += 1

print(cnt)
print(max_visit)
    
