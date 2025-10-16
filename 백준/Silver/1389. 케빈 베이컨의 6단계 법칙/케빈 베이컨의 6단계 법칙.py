import sys
from collections import deque
input = sys.stdin.readline


def bfs(x):
    visited = [-1] * (N+1)
    q = deque()
    q.append(x)
    visited[x] = 0
    while q:
        nx = q.popleft()
        for n in arr[nx]:
            if visited[n] == -1:
                q.append(n)
                visited[n] = visited[nx] + 1

    ans = sum(visited)
    return ans


N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


min_ans = float("INF") 
min_person = 0
for i in range(1, N+1):
    result = bfs(i)
    if result < min_ans:
        min_ans = result
        min_person = i
print(min_person)
