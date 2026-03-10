import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
ta, tb = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1]*(n+1)
def bfs(ta):
    q = deque()
    q.append(ta)
    visited[ta] = 0
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)

bfs(ta)
print(visited[tb])