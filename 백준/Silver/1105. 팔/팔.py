import sys

input = sys.stdin.readline

l, r = input().strip().split()

if len(l) != len(r):
    ans = 0
else:
    ans = 0
    if l == r:
        ans = l.count('8')
    else:
        for a, b in zip(l, r):
            if a == b == '8':
                ans += 1
            elif a != b:
                break

print(ans)