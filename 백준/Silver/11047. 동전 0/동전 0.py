import sys

input = sys.stdin.readline
N, K = map(int, input().split())
money_list = [int(input().strip()) for _ in range(N)]
ans = 0

for i in range(N):
    if K == 0:
        break
    ans += (K // money_list[-i-1])
    K = K % money_list[-i-1]

print(ans)