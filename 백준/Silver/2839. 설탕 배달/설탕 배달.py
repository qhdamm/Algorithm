n = int(input())

curr = n
max5 = n//5
answer = -1
while max5>=0:
    rest = curr - max5*5
    if rest % 3 == 0:
        answer = max5 + (rest//3)
        break
    max5-=1

print(answer)