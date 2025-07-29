import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def jelly(board):
    queue = deque()
    # 방문 체크
    visited = [[False] * N for _ in range(N)]
    start = (0, 0)
    queue.append(start)
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        if board[x][y] == -1:
            return "HaruHaru"
        
        new_position = board[x][y]
        if new_position == 0:
            continue

        if y + new_position < N and not visited[x][y+new_position]:
            visited[x][y+new_position] = True
            queue.append((x, y+new_position))

        if x + new_position < N and not visited[x+new_position][y]:
            visited[x+new_position][y] = True
            queue.append((x+new_position, y))
    
    return "Hing"

print(jelly(board))