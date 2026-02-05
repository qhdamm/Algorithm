import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

for _ in range(m):
    newv = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, newv)
    heapq.heappush(cards, newv)

print(sum(cards))