def solve(num):
    result_list = [0] * 10
    str_num = str(num)
    for n in str_num:
        result_list[int(n)] += 1
    return result_list

A = int(input())
B = int(input())
C = int(input())
result = solve(A*B*C)
for i in result:
    print(i)
