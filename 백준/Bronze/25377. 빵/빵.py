import sys

input = sys.stdin.readline
N = int(input())
min_time = float('INF')

for _ in range(N):
    A, B = map(int, input().split())
    if A <= B and B <= min_time:
        min_time = B

if min_time != float('INF'):
    print(min_time)
else:
    print(-1)