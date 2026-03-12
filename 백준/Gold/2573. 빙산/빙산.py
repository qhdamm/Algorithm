import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]

dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)

def count_ice():  #빙산이 몇 개 있는지?
    visited = [[False]*m for _ in range(n)]
    cnt = 0

    for r in range(n):
        for c in range(m):
            if ice[r][c] > 0 and not visited[r][c]:
                cnt += 1
                q = deque()
                q.append((r,c))
                visited[r][c] = True

                while q:
                    cr, cc = q.popleft()
                    for i in range(4):
                        nr = cr + dy[i]
                        nc = cc + dx[i]
                        if 0<=nr<n and 0<=nc<m:
                            if not visited[nr][nc] and ice[nr][nc] > 0:
                                q.append((nr, nc))
                                visited[nr][nc] = True
                    
    return cnt

def melt():  # 한번에 녹이기
    melt_graph = [[0]*m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if ice[y][x] > 0:
                melting = 0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0<=ny<n and 0<=nx<m:
                        if ice[ny][nx] == 0:
                            melting += 1
                melt_graph[y][x] = melting
    
    for y in range(n):
        for x in range(m):
            if ice[y][x] > 0:
                ice[y][x] = max(0, ice[y][x] - melt_graph[y][x])


year = 0
while True:
    cnt = count_ice()
    if cnt >= 2:
        print(year)
        break
    elif cnt == 0:
        print(0)
        break
    melt()
    year += 1
