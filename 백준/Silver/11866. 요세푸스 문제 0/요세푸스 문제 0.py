import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
queue = deque(range(1, N+1))
ans_list = []

while len(ans_list)<N:
    for _ in range(K - 1):
        num = queue.popleft()
        queue.append(num)
    ans_list.append(queue.popleft())


print("<", end="")
print(*ans_list, sep=", ", end="")
print(">")