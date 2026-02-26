import sys

input = sys.stdin.readline
bingo = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]

index_dict = {}
for r in range(5):
    for c in range(5):
        index_dict[bingo[r][c]] = (r, c)

visited_row = [False] * 5
visited_col = [False] * 5
visited_diag = [False] * 2

def check_bingo(br, bc): # index
    ans = 0
    # 가로 빙고
    if not visited_row[br] and all(bingo[br][c] == 0 for c in range(5)):
        visited_row[br] = True
        ans += 1

    # 세로 빙고
    if not visited_col[bc] and all(bingo[r][bc] == 0 for r in range(5)):
        visited_col[bc] = True
        ans += 1

    # 대각선 빙고
    if br == bc and not visited_diag[0]:  # 우하향
        if all(bingo[i][i] == 0 for i in range(5)):
            visited_diag[0] = True
            ans += 1
    if br + bc == 4 and not visited_diag[1]: # 좌하향
        if all(bingo[i][4-i] == 0 for i in range(5)):
            visited_diag[1] = True
            ans += 1

    return ans

mc_cnt = 0
bingo_cnt = 0
for i in range(5):
    for j in range(5):
        erased = mc[i][j]
        mc_cnt += 1

        r, c = index_dict[erased]
        bingo[r][c] = 0

        bingo_cnt += check_bingo(r, c)
        if bingo_cnt >= 3:
            print(mc_cnt)
            sys.exit()