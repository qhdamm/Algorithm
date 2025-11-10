import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [-1] * (n+1)
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0
    while q:
        nx = q.popleft()
        if nx == b:
            break
        for n in graph[nx]:
            if visited[n] == -1:
                q.append(n)
                visited[n] = visited[nx] + 1

bfs(a)
print(visited[b])