import sys
input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort(reverse=True)

answer = 0
for i, w in enumerate(ropes, 1):
    curr = w * i
    if curr > answer:
        answer = curr

print(answer)