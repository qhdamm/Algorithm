import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

dx = (0, 0, 1, 1, 1, -1, -1, -1)
dy = (1, -1, 0, 1, -1, 0, 1, -1)
def dfs(y,x):
    visited[y][x] = True
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <=ny< h and 0<=nx<w:
            if visited[ny][nx] != True and arr[ny][nx] != 0:
                dfs(ny, nx)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))

    ans = 0
    visited = [[False]*w for _ in range(h)]
    for j in range(h):
        for i in range(w):
            if visited[j][i] != True and arr[j][i] != 0:
                dfs(j, i)
                ans += 1

    print(ans)


