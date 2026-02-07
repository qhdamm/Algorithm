import sys
import heapq

input = sys.stdin.readline
n = int(input())
aula = [list(map(int, input().split())) for _ in range(n)]
aula.sort(key=lambda x: (x[0], x[1]))


end = [aula[0][1]]
heapq.heapify(end)
for i in range(1, n):
    s, e = aula[i]
    if end[0] <= s:
        heapq.heappop(end)
    heapq.heappush(end, e)
        
print(len(end))