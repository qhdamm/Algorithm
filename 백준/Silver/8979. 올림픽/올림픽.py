num, x = map(int,input().split())
score_list = {}
for _ in range(num):
    data = list(map(int, input().split()))
    key = data[0]
    score_list[key] = data[1:]

winners = 0
for key in score_list:
    if key == x:
        continue
   
    if score_list[x][0] < score_list[key][0]:
        winners += 1
    elif score_list[x][0] == score_list[key][0]:
        if score_list[x][1] < score_list[key][1]:
            winners += 1
        elif score_list[x][1] == score_list[key][1]:
            if score_list[x][2] < score_list[key][2]:
                winners += 1

print(winners+1)
