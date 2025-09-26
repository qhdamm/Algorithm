import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    stack = []
    data = input().strip()
    for d in data:
        if d == "(":
            stack.append(d)
        else:
            if stack: 
                stack.pop()
            else:
                stack.append("NO")
                break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")