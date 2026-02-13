import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
cards = [input().strip() for _ in range(n)]
weights = defaultdict(int) 

for card in cards:
    max_w = len(card)
    for i, c in enumerate(card):
        weights[c] += 10 ** (max_w - 1 - i)

sorted_weights = sorted(weights.items(), key=lambda x: -x[1])
assign = {}
num = 9
for c, _ in sorted_weights:
    assign[c] = num
    num -= 1

ans = 0
for c, _ in sorted_weights:
    ans += weights[c] * assign[c]

print(ans)