import sys
sys.setrecursionlimit(10**6)

def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    def dfs(start):
        visited[start] = True
        for i in range(n):
            if computers[i][start] == 1 and not visited[i]:
                dfs(i)
    
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer +=1
    
    return answer