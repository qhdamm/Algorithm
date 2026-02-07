import sys

input = sys.stdin.readline
n = int(input())
target = input().strip()

def move_right(c):
    conti = 0
    for t in target[::-1]:
        if t == c:
            conti += 1
        else:
            break
   
    return conti

def move_left(c):
    conti = 0
    for t in target:
        if t == c:
            conti += 1
        else:
            break
    return conti
    

ans1 = target.count('B') - move_right('B')
ans2 = target.count('B') - move_left('B')
ans3 = target.count('R') - move_right('R')
ans4 = target.count('R') - move_left('R')

print(min(ans1, ans2, ans3, ans4))