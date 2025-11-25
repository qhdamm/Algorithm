import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap_list = []
for _ in range(n):
    nums = map(int, input().split())
    for num in nums:
        if len(heap_list) < n:
            heapq.heappush(heap_list, num)
        else:
            if heap_list[0] < num:
                heapq.heappop(heap_list)
                heapq.heappush(heap_list, num)
               
print(heap_list[0])
