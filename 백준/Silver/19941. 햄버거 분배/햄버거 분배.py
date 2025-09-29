# 사람을 기준으로 한 윈도우에서 가장 왼쪽의 햄버거 먹기
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
ham_list = [ham for ham in input().strip()]
ans = 0

for i in range(N):
    if ham_list[i] == 'P':
        eat_window = ham_list[max(0,i-K):min(i+K+1,N)]
        for j in range(len(eat_window)):
            if eat_window[j] == 'H':
                ham_list[max(0,i-K)+j] = 'X'
                ans += 1
                break

print(ans)