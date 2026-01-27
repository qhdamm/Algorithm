import sys
input = sys.stdin.readline

n = int(input())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
alist.sort()
blist.sort(reverse=True)

answer = 0
for i in range(n):
    answer += alist[i]*blist[i]

print(answer)