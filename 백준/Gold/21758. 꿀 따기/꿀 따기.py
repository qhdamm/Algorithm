import sys

input = sys.stdin.readline
n = int(input())
honey = list(map(int, input().split()))

start = honey[0]
cumh = [start]
for i in range(1, n):
    start += honey[i]
    cumh.append(start)

ans = 0
# 1. 벌통이 맨 오른쪽: 벌1 -> 0번째, 벌2 -> i번째
for i in range(1, n-1):
    bee1 = cumh[-1] - honey[0] - honey[i]
    bee2 = cumh[-1] - cumh[i]
    ans = max(ans, bee1 + bee2)

# 2. 벌통이 맨 왼쪽: 벌1 -> n-1번째, 벌2 -> i번째
for i in range(1, n-1):
    bee1 = cumh[-1] - honey[n-1] - honey[i]
    bee2 = cumh[i-1]
    ans = max(ans, bee1 + bee2)

# 3. 벌통이 가운데: 벌1 -> 0번째, 벌2 -> n-1번째
for i in range(1, n-1):
    bee1 = cumh[i] - honey[0]
    bee2 = cumh[-1] - cumh[i-1] - honey[n-1]
    ans = max(ans, bee1 + bee2)

print(ans)