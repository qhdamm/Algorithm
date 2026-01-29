import sys
input = sys.stdin.readline

n = int(input())
scores = [int(input()) for _ in range(n)]
curr = scores[n-1]
ans = 0
for i in range(n-2, -1, -1):
    if curr <= scores[i]:
        ans += (scores[i]-curr+1)
        scores[i] = curr-1
    
    curr = scores[i]

print(ans)
