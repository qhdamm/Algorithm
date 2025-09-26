import sys
input = sys.stdin.readline
N = int(input())
stack = []

def solve():
    command = input().split()
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        if stack == []:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if stack == []:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])



for _ in range(N):
    solve()

