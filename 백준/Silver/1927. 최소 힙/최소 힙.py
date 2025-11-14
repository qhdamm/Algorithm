import sys, heapq

input = sys.stdin.readline
n = int(input())

nums = []
for _ in range(n):
    curr = int(input())
    if curr != 0:
        heapq.heappush(nums, curr)
    else:
        if len(nums) == 0:
            print(0)
        else:
            print(heapq.heappop(nums))