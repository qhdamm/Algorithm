import sys
input = sys.stdin.readline

N, K = map(int, input().split())
basket_list = [0]*K
balls = N
for i in range(K):
    basket_list[i] = i+1
    balls -= (i+1)

if balls < 0:
    print(-1)
else:
    while balls > 0:
        for i in range(1, K+1):
            basket_list[-i] += 1
            balls -= 1
            if balls == 0:
                break
    print(basket_list[-1]-basket_list[0])