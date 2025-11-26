import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
answer = []

for n in range(N, 0, -1):
    tallers = numbers[n-1]
    answer.insert(tallers, n)
    
print(*answer)