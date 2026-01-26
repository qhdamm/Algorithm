import sys
input = sys.stdin.readline

n, l = map(int, input().split())
waters = list(map(int, input().split()))
waters.sort()

answer = 1
start = waters[0] - 0.5
end = start + l
for i in range(n):
    if start <= waters[i] <= end:
        continue
    start = waters[i] - 0.5
    end = start + l
    answer += 1


print(answer)