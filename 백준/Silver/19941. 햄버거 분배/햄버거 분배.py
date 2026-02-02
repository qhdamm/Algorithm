import sys

input = sys.stdin.readline
n, k = map(int, input().split())
target = [t for t in input().strip()]

for i in range(n):
    if target[i] == "P":
        start = max(0, i-k)
        end = min(i+k+1, n)
        window = target[start:end]
        for j, t in enumerate(window):
            if t == "H":
                target[start+j] = "X"
                break

print(target.count("X"))