T = int(input())
time_lst = [300, 60, 10]
ans_lst = [0, 0, 0]
for i in range(3):
    if T // time_lst[i] == 0:
        continue
    else:
        x = T // time_lst[i]
        T -= x * time_lst[i]
        ans_lst[i] += x
if T != 0:
    print(-1)
else:
    print(ans_lst[0], ans_lst[1], ans_lst[2])


