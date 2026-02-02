import sys

input = sys.stdin.readline
n = int(input())
homes = list(map(int, input().split()))
homes.sort()
ans_idx = (n-1) // 2
print(homes[ans_idx])
