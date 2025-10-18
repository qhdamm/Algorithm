N, M = map(int, input().split())

num_list = []
visited = [False] * (N+1)
def dfs(s, d):
    if d == M:
        print(*num_list)
        return
    
    for i in range(s, N+1):
        if visited[i] == True:
            continue
        visited[i] = True
        num_list.append(i)

        dfs(i+1, d+1)
        visited[i] = False
        num_list.pop()

dfs(1, 0)

