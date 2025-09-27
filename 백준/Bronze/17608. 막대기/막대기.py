from collections import deque
import sys

input = sys.stdin.readline
queue = []
N = int(input())
for _ in range(N):
    queue.append(int(input()))
queue = deque(queue)
max_line = 0
ans = 0
while queue:
    line = queue.pop()
    if line > max_line:
        ans += 1
        max_line = line
print(ans)
