import sys
input = sys.stdin.readline

s = input().strip()
zero_num = s.count('0') // 2
one_num = s.count('1') // 2

# 1은 왼쪽부터, 0은 오른쪽부터 지우기
one_list = []
for ch in s:
    if ch == '1' and one_num > 0:
        one_num -= 1
    else:
        one_list.append(ch)

zero_list = []
for ch in reversed(one_list):
    if ch == "0" and zero_num > 0:
        zero_num -= 1
    else:
        zero_list.append(ch)

print("".join(reversed(zero_list)))
