import sys

input = sys.stdin.readline

n = int(input())

def get_fib(x):
    fib_list = [0, 1]
    while fib_list[-1] < x:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

for _ in range(n):
    target = int(input())
    fib_list = get_fib(target)
    ans = []
    for fib in fib_list[::-1]:
        if target > fib:
            ans.append(fib)
            target -= fib
        elif target < fib:
            continue
        else:
            ans.append(fib)
            break
    print(*ans[::-1])
