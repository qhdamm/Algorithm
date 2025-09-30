import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
class_list = list(map(int, input().split()))

class_sum = 0
class_sum_list = []
for c in class_list:
    class_sum += c
    class_sum_list.append(class_sum)

# [3,-5,2,-1,4] -> [3,-2,0,-1,3]
class_sum_list.sort(reverse=True)
print(sum(class_sum_list[:K]))