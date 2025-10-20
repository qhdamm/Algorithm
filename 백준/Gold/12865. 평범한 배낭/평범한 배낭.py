N, K = map(int, input().split())
W = []
V = []
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

memo = [[0] * (K+1) for _ in range(N+1)]
# def solve(n, w):   # n번째 물품에 대한 최대 v 리턴
#     if n < 0:
#         return 0
#     if memo[n][w] != -1:
#         return memo[n][w]

#     # 넣는 경우
#     new_w = w-W[n]
#     if new_w >= 0:
#         put = solve(n-1, new_w) + V[n]
#     else:
#         put = 0
#     # 안넣는 경우
#     nput = solve(n-1, w)
#     return max(put, nput)

# print(solve(n-1, k))


for n in range(N):
    for k in range(K+1):
        new_w = k - W[n]
        if new_w >= 0:
            put = memo[n-1][new_w] + V[n]
        else:
            put = 0
        nput = memo[n-1][k]
        memo[n][k] = max(put, nput)

print(memo[N-1][K])
        