import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sp = []
ep = []
for _ in range(m):
    s, e = map(int, input().split())
    if s <= e*6:
        sp.append(s)
    else:
        sp.append(e*6)
    ep.append(e)

sp.sort()
ep.sort()

r_set = n // 6
r_each = n % 6
print(min(r_set*sp[0] + r_each*ep[0], (r_set+1)*sp[0]))