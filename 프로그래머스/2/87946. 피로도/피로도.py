def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    answer = 0
    def dfs(ans, k): 
        nonlocal answer
        answer = max(answer, ans)
        if answer == n:
            return answer
        
        for i in range(n):
            need, use = dungeons[i]
            if not visited[i] and k >= need:
                visited[i] = True
                dfs(ans+1, k-use)
                visited[i] = False
                
    dfs(0, k)
    return answer


        
    
    