N = int(input())
arr = list(map(int, input().split()))

start = 0
end = N-1
abs_result = abs(arr[start] + arr[end])
start_result = arr[start]
end_result = arr[end]

while start< end:
    curr = arr[start] + arr[end]
    abs_curr = abs(curr)
    if abs_curr < abs_result:
        abs_result = abs_curr
        start_result = arr[start]
        end_result = arr[end]
    
    if curr < 0:
        start += 1
    else:
        end -= 1

print(start_result, end_result)

