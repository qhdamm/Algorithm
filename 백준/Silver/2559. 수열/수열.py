import sys

input = sys.stdin.readline
N, K = map(int, input().split())
temp_list = list(map(int, input().split()))

total = 0
sum_list = [0]*(N+1)
for i in range(N):
    total += temp_list[i]
    sum_list[i+1] = total

ans_list = [sum_list[i+K] - sum_list[i] for i in range(N-K+1)]
print(max(ans_list))