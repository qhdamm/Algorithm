import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
virused = 0
def bfs(x):
    global virused
    q = deque()
    q.append(x)
    visited[x] = True
    while q:
        nx = q.popleft()
        for nnx in graph[nx]:
            if not visited[nnx]:
                q.append(nnx)
                visited[nnx] = True
                virused += 1

bfs(1)
print(virused)