import sys

N = int(sys.stdin.readline().strip())
nuns = list(map(int, sys.stdin.readline().split()))

nuns = sorted(nuns)
answer = abs(nuns[0]+nuns[N-1]-nuns[1]-nuns[N-2])

for i in range(N):
    for j in range(i+3, N):
        sl, sr = i+1, j-1
        while sl < sr:
            now_diff = nuns[i]+nuns[j] - (nuns[sl]+nuns[sr])
            if abs(now_diff) < answer:
                answer = abs(now_diff)
            if now_diff < 0:
                sr -= 1
            else:
                sl += 1
print(answer)   
