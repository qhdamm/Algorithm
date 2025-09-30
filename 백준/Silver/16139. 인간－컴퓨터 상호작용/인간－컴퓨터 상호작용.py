import sys

input = sys.stdin.readline
text_list = [t for t in input().strip()]
N = int(input())
# (행)가로가 문자에서의 위치, (열)세로가 알파벳 -> 행 인덱스: 알파벳, 열 인덱스: 문자
count_list = [[0]*len(text_list) for _ in range(26)]

def get_index(text):
    return ord(text) - ord('a')

for i, t in enumerate(text_list):
    text_index = get_index(t)
    for j in range(26):
        count_list[j][i] = count_list[j][i-1]
    count_list[text_index][i] += 1


for _ in range(N):
    target, start, end = input().split()
    start = int(start); end = int(end)
    idx = get_index(target)
    if start == 0:
        print(count_list[idx][end])
    else:
        print(count_list[idx][end] - count_list[idx][start-1]) 