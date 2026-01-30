import sys
input = sys.stdin.readline

n = int(input())
tips = [int(input()) for _ in range(n)]
tips.sort(reverse=True)

max_tip = 0
for i in range(n):
    ct = tips[i] - i
    if ct >= 0:
        max_tip += ct

print(max_tip)
