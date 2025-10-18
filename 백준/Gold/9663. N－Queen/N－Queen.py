N = int(input())

ans = 0
width = [False] * N
diag1 = [False] * N * 2
diag2 = [False] * N * 2

def dfs(h):
    global ans

    if h == N:
        ans += 1
        return
    
    for i in range(N):
        # 대각선, 가로, 세로에 이미 퀸이 있는지 확인
        if width[i] or diag1[i+h] or diag2[h-i+N]:
            continue
        width[i] = diag1[i+h] = diag2[h-i+N] = True
        dfs(h+1)
        width[i] = diag1[i+h] = diag2[h-i+N] = False

dfs(0)
print(ans)
        
    
 