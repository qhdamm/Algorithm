import sys
from collections import deque

input = sys.stdin.readline
word = input().strip()
n = int(input())

left = list(word)
right = [] # 거꾸로 되어 잇음

for _ in range(n):
    cmd = input().split()
    
    if cmd[0] == "L":
        if left:
            right.append(left.pop())
    elif cmd[0] == "D":
        if right:
            left.append(right.pop())
    elif cmd[0] == "B":
        if left:
            left.pop()
    else:
        nw = cmd[1]
        left.append(nw)

print("".join(left + right[::-1]))