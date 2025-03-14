import sys

N, X = map(int, sys.stdin.readline().split())
visitors_list = [int(num) for num in sys.stdin.readline().split()]

current_sum = sum(visitors_list[0:X])
max_sum = current_sum
count = 1
for i in range(X, N):  # i=X부터 N-1까지 i를 하나씩 증가
    current_sum = current_sum - visitors_list[i-X] + visitors_list[i]
    if current_sum > max_sum:
        max_sum = current_sum
        count = 1
    elif current_sum == max_sum:
        count += 1

if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(count)
