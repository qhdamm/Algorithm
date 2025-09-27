import sys
from itertools import combinations

input = sys.stdin.readline
N, K = map(int, input().split())
home_list = []
for _ in range(N):
    home_list.append(list(map(int, input().split())))

def get_dist(home1, home2):
    dist = abs(home1[0]-home2[0]) + abs(home1[1]-home2[1])
    return dist

ans = 200000
# 모든 집들이 가장 가까운 오피스까지 가는 거리 중 최댓값 구하기
for combi in combinations(home_list, K):
    combi_max_dist = 0
    # 각 집에 대해 가장 가까운 오피스와의 거리 구하기 -> 그 거리 중 최댓값 구하기 = 어떤 combi에 대해 최대 거리
    for home in home_list:
        min_dist = min(get_dist(home, office) for office in combi)
        combi_max_dist = max(combi_max_dist, min_dist)
    ans = min(combi_max_dist, ans)
print(ans)