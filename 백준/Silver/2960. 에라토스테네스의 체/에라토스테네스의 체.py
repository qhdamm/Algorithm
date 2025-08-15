import sys

input = sys.stdin.readline
N, K = map(int, input().split())
num = [True] * (N+1)
num[0] = False
num[1] = False
erase = 0

for p in range(2, N+1):
    if num[p]:
        # 아직 p 가 안지워졌으니까 p의 배수 다 지우기
        for m in range(p, N+1, p):
            if num[m]:
                num[m] = False
                erase += 1
                if erase == K:
                    print(m)
                    break
