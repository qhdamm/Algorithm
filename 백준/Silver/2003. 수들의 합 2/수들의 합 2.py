import sys

N, M = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = 0
arr_sum = 0
ans = 0

while True:
    if arr_sum >= M:
        arr_sum -= arr[start]
        start += 1
    else:
        if end == N:
            break
        arr_sum += arr[end]
        end += 1
    
    if arr_sum == M:
        ans += 1

print(ans)
    
