import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
visited = [-1] * 100001
dx = (1, -1, "x")

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        x = q.popleft()
        if x == k:
            break
        for i in range(3):
            if dx[i] == "x":
                nx = 2*x
            else:
                nx = x + dx[i]
            
            if 0<=nx<=100000 and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)

bfs(n)
print(visited[k])