import sys

input = sys.stdin.readline
n = int(input())
dots = [list(map(int, input().split())) for _ in range(n)]

def get_area(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    area = abs((ax-bx)*(cy-by) - (ay-by)*(cx-bx))
    return area

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            ans = max(ans, get_area(dots[i], dots[j], dots[k]))

print(f'{ans/2:.1f}')