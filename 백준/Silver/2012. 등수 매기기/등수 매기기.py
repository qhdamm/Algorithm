import sys
input = sys.stdin.readline

n = int(input())
students = [int(input()) for _ in range(n)]
students.sort()

answer = 0
for ri in range(n):
    answer += abs(students[ri] - ri -1)

print(answer)
