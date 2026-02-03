import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    test = list(map(int, input().split()))
    
    profit = 0
    curr_max = test[-1]
    for i in range(n-1, -1, -1):
        if test[i] < curr_max:
            profit += (curr_max - test[i])
        else:
            curr_max = test[i]
    print(profit)
