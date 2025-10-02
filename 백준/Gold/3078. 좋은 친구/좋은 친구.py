import sys

input = sys.stdin.readline
N, K = map(int, input().split())
friends_list = [input().strip() for _ in range(N)]
len_list = [0] * 21
ans = 0

for i in range(N):
    cL = len(friends_list[i])
    ans += len_list[cL]
    len_list[cL] += 1

    if i >= K:
        fL = len(friends_list[i-K])
        len_list[fL] -= 1

print(ans)