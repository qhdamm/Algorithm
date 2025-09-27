import sys

input = sys.stdin.readline
N, d, k, c = map(int, input().split())
sushi_list = [int(input().strip()) for _ in range(N)]
for sushi in sushi_list[:k]:
    sushi_list.append(sushi)

ans = 0
for i in range(N):
    eat_list = sushi_list[i:i+k]
    if c not in eat_list:
        eat_list.append(c)
    ans = max(ans, len(set(eat_list)))
print(ans)