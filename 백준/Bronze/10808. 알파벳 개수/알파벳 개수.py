word = input()
ans_list = [0]*26

start = ord('a')
end = ord('z')
for w in word:
    now = ord(w)
    ans_list[now-start] += 1

print(*ans_list)
