import sys

def return_exist(num, sorted_num_list):
    start = 0
    end = len(sorted_num_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if sorted_num_list[mid]==num:
            return 1
        elif sorted_num_list[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return 0

input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
M = int(input())
target = list(map(int, input().split()))

for num in target:
    print(return_exist(num, num_list))