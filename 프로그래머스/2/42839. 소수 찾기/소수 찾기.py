from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    num_list = list(numbers)
    nums = list()
    answer = 0
    
    for i in range(1, len(num_list)+1):
        for p in permutations(num_list, i):
            nums.append(int("".join(p)))
    
    nums = set(nums)
    for n in nums:
        if is_prime(n):
            answer += 1
    
    
    return answer
