N, M = map(int, input().split())

num_list = []
visited = [False] * N
def dfs(depth):
    if depth == M:
        print(*num_list)
        return
    
    for i in range(N):
        if visited[i] == True:
            continue
        visited[i] =True
        num_list.append(i+1)
        dfs(depth+1)

        num_list.pop()
        visited[i] = False

dfs(0)

