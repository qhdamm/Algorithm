def get_sum(num):
    str_num = str(num)
    result = 0
    for st in str_num:
        result += int(st)
    return result

N = int(input())
ans = 0
for i in range(1, N+1):
    if i % get_sum(i) == 0:   
        ans += 1
print(ans)