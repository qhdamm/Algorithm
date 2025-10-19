# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
# 3 = 2+1
# 4 = 3+1
# 5 = 4+1
# 7 = 5+2

t = int(input())
ans_list = [0, 1, 1, 1, 2, 2]

def ans(n):
    for i in range(len(ans_list), n+1):
        new_ans = ans_list[i-1] + ans_list[i-5]
        ans_list.append(new_ans)
    return ans_list[n]

for _ in range(t):
    n = int(input())
    print(ans(n))