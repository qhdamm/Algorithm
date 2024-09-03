n = int(input())
for i in range(n):
    x = int(input())
    a,b,c,d = 0,0,0,0
    if x >= 25:
        a = x//25
        x = x%25
    if x >= 10:
        b = x//10
        x = x%10
    if x >= 5:
        c = x//5
        x = x%5
    if x>= 1:
        d = x
    answer = [a,b,c,d]
    print(*answer)