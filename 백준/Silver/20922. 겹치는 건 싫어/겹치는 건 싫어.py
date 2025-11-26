import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
cnts = defaultdict(int)

start = 0
ans = 0
for end in range(n):
    x = nums[end]
    cnts[x] += 1

    while cnts[x] > k:
        cnts[nums[start]] -= 1
        start += 1
    
    ans = max(ans, end - start + 1)

print(ans)