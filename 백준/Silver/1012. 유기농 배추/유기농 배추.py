import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def dfs(y, x):
    visited[y][x] = True
    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0<=nx<M and 0<=ny<N):
            continue
        if visited[ny][nx] == False and arr[ny][nx] == 1:
            dfs(ny, nx)
            


T = int(input())
for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    
    for j in range(N):
        for i in range(M):
            if arr[j][i] == 1 and visited[j][i] == False:
                dfs(j, i)
                cnt += 1
                
    print(cnt)




