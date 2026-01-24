nums = input().strip()
count_0 = 0
count_1 = 0

prev = None
for n in nums:
    if n != prev:
        if n == "0":
            count_0 += 1
        else:
            count_1 += 1
        prev = n

print(min(count_0, count_1))