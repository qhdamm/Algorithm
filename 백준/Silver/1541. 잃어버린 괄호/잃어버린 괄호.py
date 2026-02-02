import sys

input = sys.stdin.readline
target = input().strip().split('-')

for i, t in enumerate(target):
    num = 0
    if "+" in t:
        nt = map(int, t.split("+"))
        num = sum(nt)
        target[i] = num

ans = int(target[0])
for n in range(1, len(target)):
    ans -= int(target[n])

print(ans)