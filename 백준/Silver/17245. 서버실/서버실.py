n = int(input())
arr = []
for _ in range(n):
    arr += list(map(int, input().split()))
    
target = sum(arr) / 2
start = 1
end = max(arr)

result = 0
while start <= end:
    mid = (start+end)//2
    
    cnt = 0
    for i in arr:
        if i < mid:
            cnt += i
        else:
            cnt += mid
                
    if cnt < target:
        start = mid+1
    else:
        result = mid
        end = mid-1
        
print(result)