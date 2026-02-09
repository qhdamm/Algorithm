import sys

input = sys.stdin.readline
n = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
    sys.exit()

visited = [False] * m
nbox = [0] * n
ans = 0
moved = 0
while moved < m:
    for i in range(n):
        while nbox[i] < m:
            if not visited[nbox[i]] and cranes[i] >= boxes[nbox[i]]:
                visited[nbox[i]] = True
                moved += 1
                nbox[i] += 1
                break
            nbox[i] += 1
    ans += 1

print(ans)