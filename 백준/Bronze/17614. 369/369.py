N = int(input())
game = '369'
ans = 0

for i in range(1, N+1):
    for check in game:
        ans += str(i).count(check)
print(ans)