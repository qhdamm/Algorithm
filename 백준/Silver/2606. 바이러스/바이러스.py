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
def dfs(start):
    stack = [start]
    while stack:
        x = stack.pop()
        if visited[x]:
            continue
        visited[x] = True
        for next_node in graph[x]:
            if not visited[next_node]:
                stack.append(next_node)
dfs(1)
print(visited.count(True) - 1)