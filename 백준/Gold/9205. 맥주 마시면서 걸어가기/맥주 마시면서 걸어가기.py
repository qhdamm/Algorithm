import sys

input = sys.stdin.readline
t = int(input())

def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def dfs(sx, sy):
    stack = [(sy, sx)]
    while stack:
        cy, cx = stack.pop()

        if get_dist(cx, cy, ex, ey) <= 1000:
            return "happy"

        for i in range(n):
            nx, ny = convs[i]
            if not visited[i] and get_dist(cx, cy, nx, ny) <= 1000:
                visited[i] = True
                stack.append((ny, nx))
    return "sad"

for _ in range(t):
    n = int(input()) # 편의점 개수
    sx, sy = map(int, input().split()) # 출발 포인트
    convs = [list(map(int, input().split())) for _ in range(n)]
    ex, ey = map(int, input().split()) # 도착 포인트

    if get_dist(sx, sy, ex, ey) <= 1000:
        print("happy")
        continue
    
    visited = [False] * n
    ans = dfs(sx, sy)
    print(ans)
