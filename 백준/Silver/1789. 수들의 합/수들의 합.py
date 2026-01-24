s = int(input())
n = 0
curr = s
i = 1

while curr-i >= 0:
    curr -= i
    i += 1
    n += 1
print(n)