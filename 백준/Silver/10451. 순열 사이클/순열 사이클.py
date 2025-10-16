import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x):
    visited[x] = True
    for n in arr[x]:
        if visited[n] == False:
            dfs(n)


T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    arr = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for i, n in enumerate(nums):
        arr[i+1].append(n)
        arr[n].append(i+1)
    
    cnt = 0
    for i in range(1, N+1):
        if visited[i] == False:
            dfs(i)
            cnt += 1
    print(cnt)