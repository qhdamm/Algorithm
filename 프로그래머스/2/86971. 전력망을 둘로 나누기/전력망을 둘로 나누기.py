def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    answer = n
    
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)
    
    def dfs(x, visited):
        visited[x] = True
        count = 1
        for nx in graph[x]:
            if visited[nx]:
                continue
            count += dfs(nx, visited)
        return count
    
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