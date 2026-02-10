import sys

input = sys.stdin.readline
n, k = map(int, input().split())
kids = list(map(int, input().split()))

kids_diff = []
for i in range(n-1):
    kids_diff.append(kids[i+1] - kids[i])

kids_diff.sort(reverse=True)
print(sum(kids_diff[k-1:]))