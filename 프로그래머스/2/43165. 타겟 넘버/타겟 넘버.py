import sys
sys.setrecursionlimit(10**6)

def solution(numbers, target):
    answer = 0
    
    def dfs(i, curr_sum):
        
        nonlocal answer
        if i == len(numbers):
            if curr_sum == target:
                answer += 1
            return
        
        # 더하는 경우
        dfs(i+1, curr_sum + numbers[i])
        # 빼는 경우
        dfs(i+1, curr_sum - numbers[i])
    
    dfs(0, 0)
        
    return answer