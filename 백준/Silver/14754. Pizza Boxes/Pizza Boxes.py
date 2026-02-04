import sys

input = sys.stdin.readline
n, m = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(n)]

r_max = [max(row) for row in boxes]
c_max = [max(boxes[i][j] for i in range(n)) for j in range(m)]
total = sum(sum(r) for r in boxes)

keep = 0
for i in range(n):
    for j in range(m):
        if boxes[i][j] == r_max[i] or boxes[i][j] == c_max[j]:
            keep += boxes[i][j]

print(total - keep)