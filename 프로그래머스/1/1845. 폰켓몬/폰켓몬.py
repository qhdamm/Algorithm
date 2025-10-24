from collections import Counter
def solution(nums):
    get_num = len(nums) // 2
    hnum = Counter(nums)
    n_max = len(list(hnum.keys()))
    
    return min(n_max, get_num)