import sys
from collections import deque


input = sys.stdin.readline
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

visited1 = [False] * (N+1)
dfs_visit = []
def dfs(start):
    stack = [start]
    while stack:
        x = stack.pop()
        if visited1[x]:
            continue

        visited1[x] = True
        dfs_visit.append(x)
        for next_node in reversed(graph[x]):
            if not visited1[next_node]:
                stack.append(next_node)

visited2 = [False] * (N+1)
bfs_visit = []
def bfs(start):
    q = deque([start])
    visited2[start] = True
    while q:
        x = q.popleft()
        bfs_visit.append(x)

        for next_node in graph[x]:
            if not visited2[next_node]:
                visited2[next_node] = True
                q.append(next_node)

dfs(V)
bfs(V)
print(*dfs_visit)
print(*bfs_visit)