import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
dnas = [input().strip() for _ in range(n)]
order = "ACGT"

ans = []
dist = 0
for i in range(m):
    counts = Counter(dna[i] for dna in dnas)
    best = min(order, key=lambda x: (-counts[x], x))
    ans.append(best)
    dist += n - counts[best]

print("".join(ans))
print(dist)