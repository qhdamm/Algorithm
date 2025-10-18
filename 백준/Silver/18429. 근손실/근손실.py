N, K = map(int, input().split())
work = list(map(int, input().split()))

ans = 0
visited = [False] * N
def dfs(date, weight):
    global ans
    if weight < 500:
        return
    if date == N:
        ans += 1
        return
    
    weight -= K
    for i in range(N):
        if visited[i] == True:
            continue
        visited[i] = True

        dfs(date+1, weight+work[i])
        visited[i] = False

dfs(0, 500)
print(ans)