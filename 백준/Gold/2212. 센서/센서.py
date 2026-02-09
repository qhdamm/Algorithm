import sys

input = sys.stdin.readline
n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

s_dist = []
for i in range(n-1):
    s_dist.append(sensors[i+1]-sensors[i])
s_dist.sort()

if n <= k:
    print(0)
else:
    for _ in range(k-1):
        s_dist.pop()
    print(sum(s_dist))
