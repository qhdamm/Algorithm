import sys
input = sys.stdin.readline

n, m = map(int, input().split())
app = int(input())
lbask = 1
rbask = m
answer = 0
for _ in range(app):
    curr = int(input())
    if curr < lbask:
        answer += lbask-curr
        lbask = curr
        rbask = lbask + m - 1
    elif curr > rbask:
        answer += curr-rbask
        rbask = curr
        lbask = rbask-m+1

print(answer)