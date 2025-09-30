import sys

input = sys.stdin.readline
text_list = [t for t in input()]
N = int(input())

for _ in range(N):
    target, start, end = input().split()
    start = int(start); end = int(end)
    print(text_list[start:end+1].count(target))
