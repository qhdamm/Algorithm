import sys

input = sys.stdin.readline
N, d, k, c = map(int, input().split())
sushi_list = [int(input()) for _ in range(N)]
sushi_list += sushi_list[:k]
count = [0] * (d+1)

for i in range(k):
    count[sushi_list[i]] += 1

unique = sum(1 for x in count if x > 0)
eat_num = unique + (1 if count[c] == 0 else 0)
max_eat = eat_num

for i in range(k, N+k):
    left = sushi_list[i-k]
    count[left] -= 1
    if count[left] == 0:
        unique -= 1
    
    right = sushi_list[i]
    if count[right] == 0:
        unique += 1
    count[right] += 1

    eat_num = unique + (1 if count[c] == 0 else 0)
    max_eat = max(eat_num, max_eat)

print(max_eat)
