# 짝수를 다 왼쪽으로 of 홀수를 다 왼쪽으로
import sys

input = sys.stdin.readline
N = int((input()))
num_list = list(map(int, input().split()))

# 짝수를 다 왼쪽으로
# 4, 5, 1, 0, 3, 2
change1 = 0
aligned_status1 = 0
for i, x in enumerate(num_list):
    if x % 2 == 0:
        change1 += i - aligned_status1
        aligned_status1 += 1
        
# 홀수를 다 왼쪽으로
change2 = 0
aligned_status2 = 0
for i, x in enumerate(num_list):
    if x % 2 != 0:
        change2 += i - aligned_status2
        aligned_status2 += 1
    

print(min(change1, change2))