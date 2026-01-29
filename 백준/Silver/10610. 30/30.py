num = input().strip()
snums = sum(int(n) for n in num)

if '0' in num and snums%3 == 0:
    print(int(''.join(sorted(num, reverse=True))))
else:
    print(-1)