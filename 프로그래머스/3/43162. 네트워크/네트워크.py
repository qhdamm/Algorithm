import sys
sys.setrecursionlimit(10**6)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(idx):
        visited[idx] = True
        for i, node in enumerate(computers[idx]):
            if visited[i]:
                continue
            if idx != i and computers[idx][i] == 1:
                visited[i] = True
                dfs(i)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer