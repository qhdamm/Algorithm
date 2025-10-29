import sys
input = sys.stdin.readline

N = int(input())
start = input().strip()
words = [input().strip() for _ in range(N-1)]

answer = 0

for word in words:
    if abs(len(start) - len(word)) > 1:
        continue

    word_list = list(word)
    not_inc = 0
    for a in start:
        if a in word_list:
            word_list.remove(a)
        else:
            not_inc += 1
    
    more_len = len(word_list)
    total = more_len + not_inc
    if total <= 1 or (not_inc == 1 and more_len == 1):
        answer += 1

print(answer)
