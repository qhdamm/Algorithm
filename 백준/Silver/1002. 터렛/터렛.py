import sys
from math import sqrt

input = sys.stdin.readline
N = int(input())

def turret():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = sqrt((x1-x2)**2 + (y1-y2)**2)
    # 두 원이 완벽하게 일치하는 경우 -> print -1
    if  r1==r2 and x1==x2 and y1==y2:
        print(-1)
    # 두 원의 접점이 하나인 경우 -> print 1
    elif dist == (r1+r2) or dist == abs(r1-r2):
        print(1)
    # 두 원의 접점이 두개인 경우 -> print 2
    elif abs(r1-r2) < dist < (r1+r2):
        print(2)
    # 나머지 -> print 0
    else:
        print(0)


for _ in range(N):
    turret()