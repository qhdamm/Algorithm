import sys

input = sys.stdin.readline
n, kim, lim = map(int, input().split())

def get_num(person):
    if person % 2 == 0:
        new_num = person // 2
    else:
        new_num = person // 2 + 1
    return new_num

round = 1
while True:
    if (kim+1)//2 == (lim+1)//2:
        break
    kim = get_num(kim)
    lim = get_num(lim)
    round += 1

print(round)