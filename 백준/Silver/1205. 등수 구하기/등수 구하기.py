n, score, limit = map(int, input().split())
if n > 0:
    score_list = list(map(int, input().split()))
else:
    score_list = []

if n == limit and score <= score_list[-1]:
    print(-1)
else:
    ranking = 1
    for s in score_list:
        if score < s:
            ranking +=1
        elif score == s:
            break
    print(ranking)