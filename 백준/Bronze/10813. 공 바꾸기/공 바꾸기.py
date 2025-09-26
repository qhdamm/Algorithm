import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ball_list = [i+1 for i in range(N)]

def switch(x, y):
    ball_list[x-1] , ball_list[y-1] = ball_list[y-1], ball_list[x-1]
    return ball_list

for _ in range(M):
    x, y = map(int, input().split())
    ball_list = switch(x, y)

print(*ball_list)