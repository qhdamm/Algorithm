import sys

input = sys.stdin.readline
n = int(input())
payment = [list(map(int, input().split())) for _ in range(n)]
payment.sort(key=lambda x: (x[0], -x[1]))

# if all(p-d <= 0 for p, d in payment):
#     print(0)
#     sys.exit()

max_p = 0
max_b = 0
for i in range(n):
    cp = payment[i][0]
    curr_b = 0
    for j in range(i, n):
        curr_b += max(0, cp - payment[j][1])

    if curr_b > max_b:
        max_b = curr_b
        max_p = payment[i][0]

print(max_p)