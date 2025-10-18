n = int(input())
nums = [0 for _ in range(n+1)]

def tiling(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    if nums[n] > 0:
        return nums[n]
    
    nums[n] = tiling(n-1) + tiling(n-2)
    nums[n] %= 10007
    return nums[n]

print(tiling(n))