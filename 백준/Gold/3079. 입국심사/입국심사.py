import sys
input = sys.stdin.readline

N, M = map(int, input().split())
time_arr = [int(input()) for _ in range(N)]
start = 1
end = max(time_arr) * M
min_time = end

while start <= end:
    mid = (start + end) // 2
    friend_n = sum(mid // n for n in time_arr)
    if friend_n >= M:
        min_time = min(min_time, mid)
        end = mid - 1
    else:
        start = mid + 1

print(min_time)