import sys

input = sys.stdin.readline
n = int(input())
books = [int(input()) for _ in range(n)]

ans = 0
need = n
for i in range(n-1, -1, -1):
    if books[i] == need:
        need -= 1
    else:
        ans += 1

print(ans)