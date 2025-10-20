from collections import deque

def solution(maps):
    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)
    n = len(maps); m = len(maps[0])
    visited = [[-1] * m for _ in range(n)]

    q = deque()
    q.append((0,0))
    visited[0][0] = 1
        
    while q:
        y, x = q.popleft()
        if y == n-1 and x == m-1:
            return visited[y][x]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
                        
            if 0<= ny < n and 0 <= nx < m and  maps[ny][nx] == 1 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
        
    return -1