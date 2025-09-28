import sys

input = sys.stdin.readline
N = int(input())
card_list = list(map(int, input().split()))
final_ans = N

for i in range(N):
    for j in range(i+1, N):
        ans = 0

        if (card_list[j] - card_list[i]) % (j-i) != 0:
            continue
        
        diff = (card_list[j] - card_list[i]) // (j-i)
        for k in range(N):
            exp_card = card_list[i] + diff*(k-i)
            if exp_card != card_list[k]:
                ans += 1
        if ans < final_ans:
            final_ans = ans

print(final_ans)        