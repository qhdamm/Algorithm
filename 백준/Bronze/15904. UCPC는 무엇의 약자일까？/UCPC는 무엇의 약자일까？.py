import sys
input = sys.stdin.readline

target = input()
need = "UCPC"
cnt = 0

for t in target:
    if cnt < 4 and t == need[cnt]:
        cnt += 1

if cnt == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")