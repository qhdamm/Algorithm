nums = input()
count_0 = 0
count_1 = 0
flag_0 = False
flag_1 = False
for n in nums:
    if n == "1" and not flag_1:
        count_1 += 1
        flag_1 = True
        flag_0 = False
    elif n == "1" and flag_1:
        flag_1 = True
        flag_0 = False
        continue
    elif n == "0" and not flag_0:
        count_0 += 1
        flag_0 = True
        flag_1 = False
    elif n == "0" and flag_0:
        flag_0 = True
        flag_1 = False
        continue
print(min(count_0, count_1))