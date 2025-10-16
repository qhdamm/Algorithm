import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0
visited = [False]*(N+1)
def dfs(x):
    visited[x] = True
    for n in arr[x]:
        if visited[n] == False:
            dfs(n)

for i in range(1, N+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)