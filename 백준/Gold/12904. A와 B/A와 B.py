import sys

input = sys.stdin.readline
start = input().strip()
target = input().strip()

while len(start) < len(target):
    if target[-1] == 'A':
        target = target[:-1]
    else:
        target = target[:-1]
        target = target[::-1]

if target == start:
    print(1)
else:
    print(0)