from itertools import combinations
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int, input().split()))

ans = 0
for combi in combinations(num_list, 3):
    sum_num = sum(combi)
    if sum_num <= M:
        ans = max(ans, sum_num)
print(ans)