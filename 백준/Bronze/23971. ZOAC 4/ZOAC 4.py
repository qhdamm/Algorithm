import math
H, W, N, M = list(map(int, input().split(' ')))
row = math.ceil(H / (N+1))
col = math.ceil(W / (M+1))
print(row*col)