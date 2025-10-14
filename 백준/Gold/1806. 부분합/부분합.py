import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = 0
arr_sum = 0
min_len = N + 1

while True:
    if arr_sum < S:
        if end == N:
            break
        arr_sum += arr[end]
        end += 1
    else:
       min_len = min(min_len, end-start)
       arr_sum -= arr[start]
       start += 1


print(0 if min_len == N+1 else min_len)