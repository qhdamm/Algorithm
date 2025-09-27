N = int(input())

num = 1
ans = 0
while num <= N:
    for n in str(num):
        if "3" == n:
            ans += 1
        if "6" == n:
            ans += 1
        if "9" == n:
            ans += 1
    
    num += 1
print(ans)