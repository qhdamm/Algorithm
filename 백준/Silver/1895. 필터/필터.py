import sys
from typing import List

input = sys.stdin.readline
R, C = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(R)]
T = int(input())

def get_median(idxs: List[int]) -> int:
    sx, sy = idxs
    nums = []
    for i in range(3):
        nums += image[sy+i][sx:sx+3]
    nums.sort()
    return nums[4]

ans = 0
for i in range(R-2):
    for j in range(C-2):
        med = get_median([j, i])
        if med >= T:
            ans += 1

print(ans)