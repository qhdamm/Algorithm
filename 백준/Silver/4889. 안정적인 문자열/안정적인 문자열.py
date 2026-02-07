import sys

input = sys.stdin.readline
num = 1

while True:
    target = input().strip()
    if '-' in target:
        break

    q = []
    ans = 0
    for t in target:
        if t == "{":
            q.append("{")
        else:
            if q:
                q.pop()
            else:
                ans += 1
                q.append("{")
    ans += len(q) // 2
    print(f"{num}. {ans}")
    num += 1