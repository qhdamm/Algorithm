number = int(input())
pairs = []
result = 0

for _ in range(number):
    a, b = map(int, input().split())
    pairs.append([a, b])

# 가장 빨리 시작하고, 시간이 적게 걸리는 순으로 세팅
pairs.sort(key=lambda x: x[0]) # a 기준으로 정렬
pairs.sort(key=lambda x: x[1]) # b 기준으로 정렬

end_time = 0
for a, b in pairs:
    if a>= end_time:
        end_time = b
        result += 1
print(result)