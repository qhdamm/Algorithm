import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
oil = []
for _ in range(N):
    oil.append(list(map(int, input().split())))

dx = (-1, 0, 1)
answer = float('inf')
def dfs(y, x, dxi):
    global used, answer
    if y == N-1:
        answer =  min(answer, used)
        return 
    for i in range(3):
        ny = y + 1
        nx = x + dx[i]
        if 0<=nx<M and 0<=ny<N and dx[i] != dxi:
            used += oil[ny][nx]
            dfs(ny, nx, dx[i])
            used -= oil[ny][nx]

for i in range(M):
    used = oil[0][i]
    dfs(0, i, -2)

print(answer)