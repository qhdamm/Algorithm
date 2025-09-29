import sys

input = sys.stdin.readline
N, K, P = map(int, input().split())
bread = list(map(int, input().split()))

ans = 0
for i in range(0, N*K, K):
    bread_set = bread[i:(i+1)*K]
    if bread_set.count(0) < P:
        ans += 1

print(ans)