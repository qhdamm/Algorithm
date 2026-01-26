import sys
input = sys.stdin.readline

n, l = map(int, input().split())
flist = list(map(int, input().split()))
flist.sort()

for i in range(n):
    if l >= flist[i]:
        l += 1
    else:
        break
print(l)