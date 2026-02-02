import sys

input = sys.stdin.readline
a, b = input().split()

ans = 1
while int(a) < int(b):
    if b[-1] == '1':
        b = b[:-1]
        ans += 1
    elif int(b) % 2 == 0:
        nb = int(b) // 2
        b = str(nb)
        ans += 1
    else:
        break

if int(a) == int(b):
    print(ans)
else:
    print(-1)