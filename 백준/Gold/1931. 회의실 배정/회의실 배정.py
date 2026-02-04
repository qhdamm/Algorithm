import sys

input = sys.stdin.readline
n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
schedule.sort(key=lambda x: (x[1], x[0]))

ans = 1
start = schedule[0][1]
for i in range(1, n):
    if start <= schedule[i][0]:
        ans += 1
        start = schedule[i][1]

print(ans)