import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    apply = [list(map(int, input().split())) for _ in range(n)]
    apply.sort(key=lambda x: x[0])
    
    ans = 1
    curr_min = apply[0][1]
    for i in range(1, n):
        if apply[i][1] < curr_min:
            ans += 1
            curr_min = apply[i][1]
    
    print(ans)