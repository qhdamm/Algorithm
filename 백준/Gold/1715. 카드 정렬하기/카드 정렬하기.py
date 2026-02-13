import sys
import heapq

input = sys.stdin.readline
n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)

ans = 0
while len(cards) > 1:
    min1 = heapq.heappop(cards)
    min2 = heapq.heappop(cards)
    result = min1 + min2
    ans += result
    heapq.heappush(cards, result)

print(ans)