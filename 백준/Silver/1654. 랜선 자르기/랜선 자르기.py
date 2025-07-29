import sys
input = sys.stdin.readline
K, N = map(int, input().split())
line_list = []
for _ in range(K):
    line_list.append(int(input()))

line_list.sort()

start = 1
end = line_list[-1]
result = 0
while start <= end:
    mid = (start+end) // 2
    total = sum(line//mid for line in line_list)
    if total < N:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)