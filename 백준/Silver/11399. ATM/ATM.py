n = int(input())
people = list(map(int, input().split()))
people.sort()
curr = 0

answer = 0
for i in range(n):
    curr += people[i]
    answer += curr

print(answer)