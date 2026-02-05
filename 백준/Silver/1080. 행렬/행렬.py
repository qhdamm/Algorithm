import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a_mat = [list(input().strip()) for _ in range(n)]
b_mat = [list(input().strip()) for _ in range(n)]

def flip(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            a_mat[i][j] = '1' if a_mat[i][j] == '0' else '0' 

if n < 3 or m < 3:
    if a_mat == b_mat:
        print(0)
    else:
        print(-1)
        
else:
    ans = 0
    for i in range(n-2):
        for j in range(m-2):
            if a_mat[i][j] != b_mat[i][j]:
                flip(i, j)
                ans += 1
    if a_mat == b_mat:
        print(ans)
    else:
        print(-1)
