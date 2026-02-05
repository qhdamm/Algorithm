import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    trees = list(map(int, input().split()))
    trees.sort()
    
    min_score = 0
    for i in range(2, n):
        score = trees[i] - trees[i-2]
        min_score = max(score, min_score)
    print(min_score)