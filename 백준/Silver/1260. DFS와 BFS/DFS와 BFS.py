import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N, M, S = map(int, input().split())
line = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    line[a].append(b)
    line[b].append(a)

# 작은 노드부터 방문
for v in range(1, N+1):
    line[v].sort()

visited_dfs = [False]*(N+1)
ans_dfs = []
def dfs(S):
    ans_dfs.append(S)
    visited_dfs[S] = True
    for v in line[S]:
        if visited_dfs[v] != True:
            dfs(v)



visited_bfs = [False]*(N+1)
ans_bfs = []
def bfs(S):
    q = deque()
    q.append(S)
    visited_bfs[S] = True
    while q:
        x = q.popleft()
        ans_bfs.append(x)
        for v in line[x]:
            if visited_bfs[v] != True:
                visited_bfs[v] = True
                q.append(v)

dfs(S)
bfs(S)
print(*ans_dfs)
print(*ans_bfs)
                    



