import sys
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    l, h = map(int, input().split())
    lines.append((l, h))
lines.sort()

max_idx = -1; max_h = -1
for i, (l, h) in enumerate(lines):
    if h > max_h:
        max_h = h
        max_idx = i

answer = max_h

# left side
curr_l, curr_h = lines[0]
for i in range(1, max_idx+1):
    l, h = lines[i]
    answer += curr_h * (l - curr_l)
    curr_h = max(curr_h, h)
    curr_l = l

# right side
curr_l, curr_h = lines[-1]
for i in range(n-2, max_idx-1, -1):
    l, h = lines[i]
    answer += curr_h * (curr_l - l)
    curr_h = max(curr_h, h)
    curr_l = l

print(answer)