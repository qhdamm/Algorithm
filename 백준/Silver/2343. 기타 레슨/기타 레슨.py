import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lectures = list(map(int, input().split()))

# size가 주어졌을 때 몇 개의 블루레이가 필요한지 계ㅅ산
def blueray(size):
    count = 1
    total = 0
    for lecture in lectures:
        if total + lecture > size:
            count += 1
            total = lecture
        else:
            total += lecture
    return count


start = max(lectures)
result = sum(lectures)

end = sum(lectures)
while start <= end:
    mid = (start + end) // 2
    if blueray(mid) <= M:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)