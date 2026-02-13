import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
l = min(n, m)

for k in range(l, 0, -1):
    for i in range(n-k+1):
        for j in range(m-k+1):
            lu = board[i][j]
            ru = board[i][j+k-1]
            ld = board[i+k-1][j]
            rd = board[i+k-1][j+k-1]
            
            if lu == ru == ld == rd:
                print(k*k)
                sys.exit()
    k -= 1

print(1)