import sys

input = sys.stdin.readline
k = int(input())
choco = 2
while choco < k:
    choco *= 2

ans_choco = choco
split = 0
while choco > 0:
    if k > choco:
        k -= choco
    elif k == choco:
        break
    else:
        choco //= 2
        split += 1

print(ans_choco, split)
