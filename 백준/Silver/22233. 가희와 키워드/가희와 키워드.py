import sys

input = sys.stdin.readline
n, m = map(int, input().split())
words = []
for _ in range(n):
    words.append(input().strip())
words = set(words)

for i in range(m):
    used = set(input().strip().split(","))
    words -= used
    print(len(words))
