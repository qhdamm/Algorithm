import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
arr = [[] for _ in range(N+1)]
for i in range(1, N+1):
    a = int(input())
    arr[i].append(a)

ans = []
def dfs(s, x):
    visited[x] = True
    for n in arr[x]:
        if visited[n] == False:
            dfs(s, n)
        elif s == n:
            ans.append(s)
            return

for i in range(1, N+1):
    visited = [False]*(N+1)
    if visited[i] == False:
        dfs(i, i)

ans.sort()
print(len(ans))
for a in ans:
    print(a)