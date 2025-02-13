s_num = int(input())
s_list = list(map(int, input().split()))
p_num = int(input())
x = 0
for _ in range(p_num):
    gender, number = map(int, input().split())
    if gender == 1:
        for i in range(number, s_num+1, number):
            s_list[i-1] = 1 - s_list[i-1]

    elif gender == 2:
        number -= 1
        left, right = number, number
        while left >= 0 and right <s_num and s_list[left] == s_list[right]:
            left -= 1
            right += 1
        left += 1
        right -= 1
        for i in range(left, right+1):
            s_list[i] = 1-s_list[i]
for i in range(0, s_num, 20):
    print(*s_list[i:i+20])