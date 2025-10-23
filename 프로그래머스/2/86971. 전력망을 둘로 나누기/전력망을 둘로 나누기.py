def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
    
    
    def dfs(node, visited):
        num = 1
        visited[node] = True
        for nx in graph[node]:
            if visited[nx]:
                continue
            num += dfs(nx, visited)
        return num
    
    answer = n
    for cx, cy in wires:
        graph[cx].remove(cy)
        graph[cy].remove(cx)
        
        visited = [False] * (n+1)
        size1 = dfs(cx, visited)
        size2 = n - size1
        answer = min(answer, abs(size1-size2))
        
        graph[cx].append(cy)
        graph[cy].append(cx)
        
    return answer