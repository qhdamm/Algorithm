import sys
from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [-1] * (f+1)

q = deque()
q.append(s)
visited[s] = 0
while q:
    curr = q.popleft()
    if curr == g:
        break

    up = curr + u
    if 0<up<=f and visited[up] == -1:
        visited[up] = visited[curr]+1
        q.append(up)

    dw = curr - d
    if 0<dw<=f and visited[dw] == -1:
        visited[dw] = visited[curr] + 1
        q.append(dw)

if visited[g] == -1:
    print("use the stairs")
else:
    print(visited[g])