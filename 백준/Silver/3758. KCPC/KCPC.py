import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k, me, m = map(int, input().split())
    scores = {i: [0]*(k+1) for i in range(1, n+1)}
    cnt = [0] * (n+1)
    last_order = [0] * (n+1)

    for num in range(m):
        i, j, s = map(int, input().split())
        scores[i][j] = max(scores[i][j], s)
        cnt[i] += 1
        last_order[i] = num
    
    ranking = sorted(scores, key=lambda x: (-sum(scores[x]), cnt[x], last_order[x]))
    print(ranking.index(me)+1)