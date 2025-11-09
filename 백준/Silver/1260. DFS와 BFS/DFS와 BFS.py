import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i] = sorted(graph[i])

visited = [False] * (n+1)
dfs_visit = []
def dfs(x):
    visited[x] = True
    dfs_visit.append(x)
    for n in graph[x]:
        if visited[n]:
            continue
        dfs(n)

visited2 = [False] * (n+1)
bfs_visit = []
def bfs(x):
    q = deque()
    q.append(x)
    visited2[x] = True
    while q:
        nx = q.popleft()
        bfs_visit.append(nx)
        for n in graph[nx]:
            if visited2[n]:
                continue
            q.append(n)
            visited2[n] = True

dfs(v)
bfs(v)
print(*dfs_visit)
print(*bfs_visit)