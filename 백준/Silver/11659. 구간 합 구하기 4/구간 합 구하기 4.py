import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
cum_list = [0] * (N+1)

value = 0
for i, num in enumerate(num_list):
    value += num
    cum_list[i+1] = value

for _ in range(M):
    i, j = map(int, input().split())
    print(cum_list[j] - cum_list[i-1])