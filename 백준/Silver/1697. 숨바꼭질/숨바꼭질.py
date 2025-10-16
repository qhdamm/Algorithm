import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
move_list = [1, -1, "x"]

visited = [-1] * 100001
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0
    while q:
        n = q.popleft()
        if n == K:
            break
        for i in range(3):
            if move_list[i] == "x":
                nx = 2 * n
            else:
                nx = n + move_list[i]
            
            if 0<=nx<=100000 and visited[nx] == -1:
                visited[nx] = visited[n] + 1
                q.append(nx)
            
bfs(N)
print(visited[K])